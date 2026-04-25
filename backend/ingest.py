"""Parse the Dutch-law enforceability taxonomy markdown into structured chunks
and build a local embedding store for retrieval.

Run once before starting the API:
    python -m backend.ingest
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

ROOT = Path(__file__).resolve().parent.parent
TAXONOMY_FILE = ROOT / "taxonomy" / "dutch_law_enforceability.md"
DATA_DIR = ROOT / "data"
CHUNKS_FILE = DATA_DIR / "chunks.json"
EMBEDDINGS_FILE = DATA_DIR / "embeddings.npy"

EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"


@dataclass
class Chunk:
    rag_tag: str
    section: str            # e.g. "A5"
    title: str              # e.g. "Strijd met openbare orde of goede zeden"
    part: str               # "A", "B", "C", "D", "E"
    part_label: str         # e.g. "MATERIAL VALIDITY GROUNDS"
    body: str               # full markdown body for this entry


HEADING_RE = re.compile(r"^###\s+([A-E]\d+)\.\s+(.+?)\s*$")
RAG_TAG_RE = re.compile(r"\*\*RAG_TAG:\*\*\s*`([^`]+)`")
PART_RE = re.compile(r"^##\s+PART\s+([A-E])\s+[—-]\s+(.+?)\s*$", re.IGNORECASE)


def parse_taxonomy(text: str) -> list[Chunk]:
    """Parse the taxonomy markdown into Chunk objects, one per entry (A1, A2, ...)."""
    chunks: list[Chunk] = []
    current_part = ""
    current_part_label = ""
    # Split on lines to find section boundaries.
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        part_match = PART_RE.match(line)
        if part_match:
            current_part = part_match.group(1).upper()
            current_part_label = part_match.group(2).strip()
            i += 1
            continue

        heading_match = HEADING_RE.match(line)
        if heading_match:
            section = heading_match.group(1)
            title = heading_match.group(2).strip()
            # Collect body until next heading (### ... or ## ... or --- separator before next ###).
            body_lines = [line]
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                if HEADING_RE.match(nxt) or PART_RE.match(nxt):
                    break
                body_lines.append(nxt)
                j += 1
            body = "\n".join(body_lines).strip()
            # Strip trailing "---" separators from body.
            body = re.sub(r"\n-{3,}\s*$", "", body).strip()

            rag_tag_match = RAG_TAG_RE.search(body)
            if not rag_tag_match:
                # Skip entries without a RAG_TAG (shouldn't happen in this doc).
                i = j
                continue
            rag_tag = rag_tag_match.group(1)

            chunks.append(
                Chunk(
                    rag_tag=rag_tag,
                    section=section,
                    title=title,
                    part=current_part,
                    part_label=current_part_label,
                    body=body,
                )
            )
            i = j
            continue
        i += 1
    return chunks


def build_embedding_text(chunk: Chunk) -> str:
    """What we actually embed for retrieval — title + body, but trim heavy citation noise."""
    # Keep the whole body; the multilingual model handles Dutch + English well.
    return f"{chunk.section}. {chunk.title}\n\n{chunk.body}"


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    text = TAXONOMY_FILE.read_text(encoding="utf-8")
    chunks = parse_taxonomy(text)
    if not chunks:
        raise SystemExit("No chunks parsed — check taxonomy file format.")

    print(f"Parsed {len(chunks)} chunks.")
    for c in chunks:
        print(f"  {c.section:>3}  {c.rag_tag}")

    print(f"\nLoading embedding model: {EMBEDDING_MODEL}")
    model = SentenceTransformer(EMBEDDING_MODEL)
    texts = [build_embedding_text(c) for c in chunks]
    print(f"Embedding {len(texts)} chunks...")
    embeddings = model.encode(
        texts,
        batch_size=16,
        show_progress_bar=True,
        normalize_embeddings=True,
    )

    CHUNKS_FILE.write_text(
        json.dumps([asdict(c) for c in chunks], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    np.save(EMBEDDINGS_FILE, embeddings.astype(np.float32))
    print(f"\nWrote {CHUNKS_FILE}")
    print(f"Wrote {EMBEDDINGS_FILE} (shape={embeddings.shape}, dtype=float32)")


if __name__ == "__main__":
    main()
