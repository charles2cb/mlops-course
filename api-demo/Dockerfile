# Dockerfile
FROM python:3.10

WORKDIR /api-demo

# Install deps first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt uvicorn

# Copy source
COPY . .
EXPOSE 8000

# Example: FastAPI
RUN useradd app
USER app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
