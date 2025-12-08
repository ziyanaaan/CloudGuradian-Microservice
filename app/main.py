from fastapi import FastAPI
import psutil
from datetime import datetime

app= FastAPI()

@app.get("/")
def runstat():
    return "App is running"

@app.get("/health")
def healthstat():
    return "Status : Healthy"

@app.get("/status/server")
def serverHealth():
    return "Server is healthy"

@app.get("/status/cpu")
def getCpuStat():
    cpu_use = psutil.cpu_percent(interval=1)
    return { 
        "Status": "Running",
            "CPU usage" : cpu_use
        }

@app.get("/current-time")
def get_current_time():
    now = datetime.now()
    
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    return {
        "status": "success",
        "timestamp": formatted_time
    }
