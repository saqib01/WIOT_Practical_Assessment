# main.py
from fastapi import FastAPI, Request
from datetime import datetime

app = FastAPI()

# In-memory store (use DB in production)
logged_ips = []

@app.post("/log-ip")
async def log_ip(request: Request):
    # Get client IP (handles proxy headers too)
    client_ip = request.client.host

    log_entry = {
        "ip": client_ip,
        "timestamp": datetime.utcnow().isoformat()
    }

    logged_ips.append(log_entry)
    return {"message": "IP logged successfully", "entry": log_entry}


@app.get("/logs")
async def get_logs():
    return {"logs": logged_ips}

