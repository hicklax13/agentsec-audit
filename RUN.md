# RUN.md — Operational Manual & Daily Rhythm

## 1. Daily Autonomous Operating Cycle
Every 24 hours, the AI agent operating AgentSec Audit performs the following cycle:

1. **Vulnerability Database Sync (04:00 UTC):**
   - Scrapes OWASP GenAI Security feeds, GitHub Advisory Database, and CVE feeds for emerging agentic attack patterns.
   - Automatically updates `agentsec/rules.json` and issues a pull request.
2. **Lead Generation & Outreach (13:00 UTC):**
   - Scans GitHub trending repositories with topics `ai-agent`, `mcp-server`, `crewai`, `langchain`, `autogen`.
   - Runs `scripts/prospect_scanner.py` to identify repositories with unauthenticated tool definitions or vulnerable prompt injections.
   - Generates customized audit briefs and saves them to `outreach/queued_pitches.json`.
3. **Usage & Churn Telemetry Check (18:00 UTC):**
   - Queries Stripe webhooks and telemetry endpoints.
   - Generates a daily summary of active scans, paid conversions, and customer support tickets.

---

## 2. Running the Tool Locally (Quickstart)

### Prerequisites
- Python 3.10+ installed
- Pip packages: `fastapi`, `uvicorn`, `pydantic` (optional for local API server)

### Command-line Interface
```bash
# Run a scan against a sample agent configuration file or MCP manifest
python -m src.cli scan ./sample_agent.json

# Export an audit report to HTML
python -m src.cli scan ./sample_agent.json --format html --out report.html

# Run the API server
python -m src.server
```

---

## 3. Deployment Commands
```bash
# Deploy landing page & API to Vercel
npx vercel --prod

# Or run with Docker
docker build -t agentsec-scanner .
docker run -p 8080:8080 agentsec-scanner
```
