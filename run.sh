#!/usr/bin/env bash
# One-shot setup + launch. Run from the project root.
set -e

cd "$(dirname "$0")"

if [ ! -d ".venv" ]; then
  echo "Creating virtualenv at .venv"
  python3 -m venv .venv
fi

# shellcheck disable=SC1091
source .venv/bin/activate

echo "Installing dependencies..."
pip install --quiet --upgrade pip
pip install --quiet -r requirements.txt

if [ ! -f ".env" ]; then
  if [ -f ".env.example" ]; then
    cp .env.example .env
    echo ""
    echo "Created .env from .env.example — edit it and add your ANTHROPIC_API_KEY,"
    echo "then run this script again."
    exit 1
  fi
fi

# Build the embedding store if missing.
if [ ! -f "data/embeddings.npy" ] || [ ! -f "data/chunks.json" ]; then
  echo "Building taxonomy embedding store (one-time)..."
  python -m backend.ingest
fi

PORT=${PORT:-8001}
echo ""
echo "Starting server at http://localhost:$PORT"
exec uvicorn backend.app:app --host 0.0.0.0 --port "$PORT"
