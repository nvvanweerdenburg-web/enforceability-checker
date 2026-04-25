"""Claude-based enforceability analysis.

Given a document + a set of retrieved taxonomy chunks, produces a structured
enforceability report (JSON). Prompt caching is enabled on the taxonomy block
so that repeated calls in the same ~5-minute window amortise the cost of the
big context."""

from __future__ import annotations

import json
import os
import re
from typing import Any

from anthropic import Anthropic

MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6")
MAX_TOKENS = int(os.environ.get("ANTHROPIC_MAX_TOKENS", "8192"))

_client: Anthropic | None = None


def _get_client() -> Anthropic:
    global _client
    if _client is None:
        if not os.environ.get("ANTHROPIC_API_KEY"):
            raise RuntimeError(
                "ANTHROPIC_API_KEY is not set. Copy .env.example to .env and fill it in."
            )
        _client = Anthropic()
    return _client


SYSTEM_INSTRUCTIONS = """You are an expert Dutch contract-law analyst. You evaluate
whether clauses in a submitted document are **enforceable** under Dutch civil,
procedural, and insolvency law, using the taxonomy of grounds provided in the
context.

Rules:
- Use only the taxonomy entries supplied. If a clause does not clearly map to
  one of them, say so rather than invent a ground.
- For each finding, reference the taxonomy entry by its RAG_TAG (e.g.
  `nl.bw.3_40_1.openbare_orde_goede_zeden`) and section code (e.g. "A5").
- Distinguish clearly between **nietig** (void ab initio) and **vernietigbaar**
  (voidable — requires invocation), and note who may invoke.
- Quote the exact problematic language from the document (max ~25 words per
  quote) so the user can locate it.
- Be concrete: explain *why* the clause triggers the ground, not just that it
  does.
- If the document is not a contract / legal instrument, say so and stop.
- Write findings in English; keep the original Dutch statutory terminology
  (e.g. "wilsgebrek", "ambtshalve", "strekking-toets") where natural.

Output a single JSON object with this schema — no prose before or after:

{
  "document_type": "short description of what the document is",
  "language": "detected language of the document (e.g. 'Dutch', 'English')",
  "overall_assessment": "1-3 sentence summary of the enforceability picture",
  "overall_risk": "low" | "medium" | "high",
  "findings": [
    {
      "clause_quote": "verbatim snippet from the document",
      "issue": "short label of the problem",
      "rag_tag": "matching RAG_TAG from taxonomy",
      "section": "A1 / B3 / D2 / etc.",
      "qualification": "nietig" | "vernietigbaar" | "niet-afdwingbaar" | "geldig_maar_beperkt" | "other",
      "who_can_invoke": "who under Dutch law",
      "reasoning": "2-5 sentences explaining the analysis",
      "severity": "low" | "medium" | "high",
      "suggested_fix": "optional — how to cure the defect, or null"
    }
  ],
  "caveats": ["free-form caveats, e.g. uncertainties, missing context, cases where low-confidence taxonomy entries were used"]
}
"""


def build_taxonomy_block(chunks: list[dict]) -> str:
    """Format retrieved taxonomy chunks into a single text block."""
    parts = []
    for c in chunks:
        parts.append(
            f"### {c['section']}. {c['title']}  \n"
            f"RAG_TAG: `{c['rag_tag']}`  \n"
            f"Part: {c['part']} — {c['part_label']}\n\n"
            f"{c['body']}"
        )
    return "\n\n---\n\n".join(parts)


def analyze_document(document_text: str, retrieved_chunks: list[dict]) -> dict[str, Any]:
    """Call Claude with the document and retrieved taxonomy; return parsed JSON."""
    client = _get_client()

    taxonomy_block = build_taxonomy_block(retrieved_chunks)

    # Structure: system (cacheable) + user turn.
    # Put the taxonomy in the system block with cache_control so repeated
    # analyses in a 5-minute window reuse the cached prefix.
    system = [
        {"type": "text", "text": SYSTEM_INSTRUCTIONS},
        {
            "type": "text",
            "text": (
                "Below is the applicable Dutch-law enforceability taxonomy you must "
                "use for this analysis. Each entry is keyed by a stable RAG_TAG:\n\n"
                + taxonomy_block
            ),
            "cache_control": {"type": "ephemeral"},
        },
    ]

    user_message = (
        "Analyse the following document for enforceability issues under Dutch law. "
        "Map problematic clauses to the RAG_TAGs from the taxonomy above and return "
        "the JSON report.\n\n"
        "=== DOCUMENT START ===\n"
        f"{document_text}\n"
        "=== DOCUMENT END ==="
    )

    resp = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=system,
        messages=[{"role": "user", "content": user_message}],
    )

    raw = "".join(block.text for block in resp.content if getattr(block, "type", None) == "text")
    return _parse_json(raw)


def _parse_json(raw: str) -> dict[str, Any]:
    """Extract the first JSON object from the model's output.
    The system prompt asks for pure JSON but we defensively strip fences / prose,
    and attempt to repair common formatting issues."""
    s = raw.strip()
    # Strip ```json fences if present.
    fence = re.search(r"```(?:json)?\s*(.*?)```", s, re.DOTALL)
    if fence:
        s = fence.group(1).strip()
    # Find the first {...} object, being careful about nesting.
    start = s.find("{")
    if start == -1:
        raise ValueError(f"Model returned no JSON object. Raw output:\n{raw}")

    # Scan from start, counting braces to find the matching close.
    depth = 0
    in_string = False
    escape_next = False
    end = -1
    for i in range(start, len(s)):
        c = s[i]
        if escape_next:
            escape_next = False
            continue
        if c == "\\":
            escape_next = True
            continue
        if c == '"' and not escape_next:
            in_string = not in_string
            continue
        if in_string:
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break

    if end == -1:
        # Likely truncated due to token limit.
        raise ValueError(
            f"Model output appears truncated (unbalanced JSON braces). "
            f"This usually means the document is too long or MAX_TOKENS is too low. "
            f"Try increasing ANTHROPIC_MAX_TOKENS in .env (current: {MAX_TOKENS}). "
            f"First 1000 chars of raw output:\n{raw[:1000]}"
        )

    candidate = s[start:end]
    try:
        return json.loads(candidate)
    except json.JSONDecodeError as e:
        # Try a lenient repair: replace literal newlines in strings with \n
        # (This is a band-aid; ideally Claude would output valid JSON.)
        try:
            repaired = re.sub(r':\s*"([^"]*\n[^"]*)"', lambda m: ': "' + m.group(1).replace('\n', '\\n').replace('\r', '\\r') + '"', candidate)
            return json.loads(repaired)
        except json.JSONDecodeError:
            raise ValueError(f"Failed to parse JSON from model output: {e}\n\nCandidate:\n{candidate[:500]}...") from e
