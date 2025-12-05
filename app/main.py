from fastapi import FastAPI
from models import Product

app= FastAPI()

@app.get("/")
def runstat():
    return "App is running"

@app.get("/health")
def healthstat():
    return "Status : Healthy"