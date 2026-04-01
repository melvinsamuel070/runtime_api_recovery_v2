#!/bin/bash

# Run fix script
bash /app/solution/fix.sh

# Start the FastAPI server
uvicorn main:app --host 0.0.0.0 --port 8000 &

# Wait for server to start
sleep 5