"""Cosine-similarity retriever over the pre-computed taxonomy embeddings."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
CHUNKS_FILE = DATA_DIR / "chunks.json"
EMBEDDINGS_FILE = DATA_DIR / "embeddings.npy"
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"


@lru_cache(maxsize=1)
def _load() -> tuple[list[dict], np.ndarray, SentenceTransformer]:
    if not CHUNKS_FILE.exists() or not EMBEDDINGS_FILE.exists():
        raise FileNotFoundError(
            "Taxonomy store not found. Run `python -m backend.ingest` first."
        )
    chunks = json.loads(CHUNKS_FILE.read_text(encoding="utf-8"))
    embeddings = np.load(EMBEDDINGS_FILE)  # already L2-normalised
    model = SentenceTransformer(EMBEDDING_MODEL)
    return chunks, embeddings, model


def retrieve(query: str, top_k: int = 5) -> list[dict]:
    """Return the top-k most relevant taxonomy chunks for `query`, with scores."""
    chunks, embeddings, model = _load()
    q = model.encode([query], normalize_embeddings=True)[0].astype(np.float32)
    scores = embeddings @ q
    idx = np.argsort(-scores)[:top_k]
    results = []
    for i in idx:
        c = dict(chunks[int(i)])
        c["score"] = float(scores[int(i)])
        results.append(c)
    return results


def retrieve_many(queries: list[str], top_k_per_query: int = 3, cap: int = 20) -> list[dict]:
    """Retrieve for each query, then return a deduplicated union (highest score wins),
    capped at `cap` items ordered by best score."""
    best: dict[str, dict] = {}
    for q in queries:
        for hit in retrieve(q, top_k=top_k_per_query):
            tag = hit["rag_tag"]
            prev = best.get(tag)
            if prev is None or hit["score"] > prev["score"]:
                best[tag] = hit
    ordered = sorted(best.values(), key=lambda x: x["score"], reverse=True)
    return ordered[:cap]


def load_all_chunks() -> list[dict]:
    chunks, _, _ = _load()
    return [dict(c) for c in chunks]
