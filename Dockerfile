FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for PDF extraction, etc.
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Build embedding store on startup (ingest runs once, data persists in mounted volume)
CMD python -m backend.ingest && \
    uvicorn backend.app:app --host 0.0.0.0 --port $PORT
