FROM python:3.12-slim

WORKDIR /app

# Copy all files into container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]