# AgentSec Audit

> The security gate for autonomous AI agents. Lints system prompts, tool schemas, and MCP server manifests against the **OWASP Top 10 for Agentic Applications (2026 ASI01–ASI10)**, auto-remediates violations, and issues compliance PDFs.

![demo](https://raw.githubusercontent.com/hicklax13/agentsec-audit/master/public/demo.gif)

---

## What it catches (real findings from the shipped engine)

| Code | Finding | One-command fix |
|------|---------|-----------------|
| ASI01 | Prompt injection with no instruction boundary | `agentsec fix` injects `<user_data>` isolation |
| ASI02 | Destructive ops without human confirmation | two-phase confirmation gate |
| ASI03 | Plaintext credentials hardcoded in MCP env blocks | vault reference `${TOKEN}` |
| ASI05 | Arbitrary shell execution exposed to the agent | sandboxed microVM + HITL gate |
| ASI06 | Unbounded recursive agent delegation | max_depth + turn budget |
| ASI07 | Unencrypted HTTP transport for remote MCP | upgrade to HTTPS |

Traditional code linters (Snyk) and prompt guardrails (LlamaGuard) both stop short of the agent execution loop. That gap is this tool.

---

## Quickstart

```bash
git clone https://github.com/hicklax13/agentsec-audit.git
cd agentsec-audit
pip install -e .

# audit an agent config
agentsec scan ./sample_agent.json

# automatically remediate violations
agentsec fix ./sample_agent.json

# re-scan: 100/100 PASSED
agentsec scan ./sample_agent.json

# generate signed compliance PDF evidence
agentsec scan ./sample_agent.json --format pdf --out audit.pdf
```

## GitHub Action Integration

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

## MCP-Native

Runs as a Model Context Protocol server, so agents in Hermes Desktop, Claude Code, and Codex can audit their own configs before commit:

```bash
python -m agentsec.mcp_server
```

Exposes `audit_agent_config` over stdio JSON-RPC.

## Pricing

- **Developer:** free forever (this repo)
- **Team CI/CD:** $49/mo — PR gating + auto-fix patches
- **Compliance Pro:** $249/mo — signed SOC 2 / ISO 42001 PDF packs

## Disclaimer

Audit reports are heuristic, point-in-time automated assessments. They are not a legal guarantee or a defense against zero-day exploits. Provided AS IS.

MIT licensed.
