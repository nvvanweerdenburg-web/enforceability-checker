"""FastAPI entrypoint for the Dutch-law enforceability checker.

Run locally:
    uvicorn backend.app:app --reload --port 8000

Endpoints:
    POST /api/check        — upload a document, get a structured report
    POST /api/check-text   — submit raw text, get a structured report
    GET  /api/taxonomy     — list all taxonomy entries (diagnostic)
    GET  /                 — serve the frontend UI
"""

from __future__ import annotations

import os
from pathlib import Path

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

# Load .env if present (optional — skip silently if python-dotenv not installed)
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

from backend import analyzer, extractor, retriever

ROOT = Path(__file__).resolve().parent.parent
FRONTEND_DIR = ROOT / "frontend"

MAX_UPLOAD_BYTES = int(os.environ.get("MAX_UPLOAD_BYTES", str(10 * 1024 * 1024)))  # 10 MB
MAX_DOC_CHARS = int(os.environ.get("MAX_DOC_CHARS", str(120_000)))

app = FastAPI(title="Dutch Enforceability Checker")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def _run_pipeline(document_text: str) -> dict:
    document_text = document_text.strip()
    if not document_text:
        raise HTTPException(status_code=400, detail="Document is empty.")
    if len(document_text) > MAX_DOC_CHARS:
        raise HTTPException(
            status_code=413,
            detail=f"Document too large ({len(document_text)} chars; limit {MAX_DOC_CHARS}).",
        )

    doc_chunks = extractor.chunk_document(document_text)
    if not doc_chunks:
        raise HTTPException(status_code=400, detail="No readable text in document.")

    # Retrieve taxonomy entries per doc chunk, then merge.
    retrieved = retriever.retrieve_many(doc_chunks, top_k_per_query=4, cap=18)

    report = analyzer.analyze_document(document_text, retrieved)
    report["_retrieved_tags"] = [
        {"rag_tag": c["rag_tag"], "section": c["section"], "title": c["title"], "score": round(c["score"], 3)}
        for c in retrieved
    ]
    report["_doc_chars"] = len(document_text)
    return report


@app.post("/api/check")
async def check_upload(file: UploadFile = File(...)) -> JSONResponse:
    raw = await file.read()
    if len(raw) > MAX_UPLOAD_BYTES:
        raise HTTPException(status_code=413, detail=f"File too large (limit {MAX_UPLOAD_BYTES} bytes).")
    try:
        text = extractor.extract_text(file.filename or "upload", raw)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Extraction failed: {e}")

    try:
        report = _run_pipeline(text)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {e}")

    return JSONResponse(report)


@app.post("/api/check-text")
async def check_text(text: str = Form(...)) -> JSONResponse:
    try:
        report = _run_pipeline(text)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {e}")
    return JSONResponse(report)


@app.get("/api/taxonomy")
async def list_taxonomy() -> JSONResponse:
    chunks = retriever.load_all_chunks()
    summary = [
        {
            "section": c["section"],
            "title": c["title"],
            "rag_tag": c["rag_tag"],
            "part": c["part"],
            "part_label": c["part_label"],
        }
        for c in chunks
    ]
    return JSONResponse({"count": len(summary), "entries": summary})


# --- Static frontend ---
if FRONTEND_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")

    @app.get("/")
    async def root():
        index = FRONTEND_DIR / "index.html"
        if index.exists():
            return FileResponse(str(index))
        return JSONResponse({"message": "Frontend not found — POST to /api/check."})
