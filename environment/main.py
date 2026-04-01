from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

class ServiceStatus(BaseModel):
    service: str

PORT = os.getenv("PORT")  # intentionally unused/misconfigured

@app.get("/status", response_model=ServiceStatus)
def get_status():
    return {"service": "running"}