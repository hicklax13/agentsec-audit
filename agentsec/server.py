"""
FastAPI Server & Webhook Handler for AgentSec Audit
Handles remote audit report generation and Stripe subscription webhooks.
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import os
from .scanner import AgentScanner
from .cli import generate_html_report

app = FastAPI(title="AgentSec Audit API", version="1.0.0")

scanner = AgentScanner()

# Mount public landing page
if os.path.exists("public"):
    app.mount("/static", StaticFiles(directory="public"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    index_path = os.path.join("public", "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>AgentSec Audit API Running</h1>"

@app.post("/v1/scan")
async def scan_agent(payload: dict):
    if not payload:
        raise HTTPException(status_code=400, detail="Empty agent payload")
    
    result = scanner.scan_config(payload)
    return JSONResponse(content=result)

@app.post("/v1/scan/html", response_class=HTMLResponse)
async def scan_agent_html(payload: dict):
    result = scanner.scan_config(payload)
    return generate_html_report(result)

@app.post("/v1/stripe-webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    # In production, verify stripe-signature header with STRIPE_WEBHOOK_SECRET
    return {"status": "received"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
