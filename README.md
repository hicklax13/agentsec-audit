# AgentSec Audit

> Automated security scanning, policy linting, and compliance certification for autonomous AI agents, tool configurations, and Model Context Protocol (MCP) servers.

Built for the **OWASP Top 10 for Agentic Applications (2026 ASI01–ASI10)** and **ISO 42001 / SOC 2 Type II** processing integrity audits.

---

## Features
- **Deterministic Static AST & Schema Linter:** Scans system prompts, function calling schemas, and MCP tool declarations.
- **OWASP ASI-10 Rule Enforcement:** Detects arbitrary shell/eval execution, goal hijacking vectors, unbounded delegation depth, and unsanitized memory write loops.
- **Native MCP Interface:** Exposes `audit_agent_config` over stdio JSON-RPC so Hermes Desktop, Claude Code, and Codex can audit agents natively.
- **Turnkey CI/CD:** Ready for GitHub Actions with automated PR pass/fail gating.

---

## Quickstart

### Installation
```bash
git clone https://github.com/hicklax13/agentsec-audit.git
cd agentsec-audit
pip install -r requirements.txt
```

### Run a Local Security Audit
```bash
python -m src.cli scan ./sample_agent.json --format html --out report.html
```

---

## GitHub Action Integration
Add this to your repository workflow:
```yaml
name: AgentSec Compliance Check
on: [push, pull_request]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: hicklax13/agentsec-audit@v1
        with:
          config-path: "agent.json"
          fail-on-violation: "true"
```
