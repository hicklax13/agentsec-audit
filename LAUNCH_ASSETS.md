# Launch & Distribution Assets: AgentSec Audit

## 1. Show HN Pitch (Hacker News)

**Title:** Show HN: AgentSec Audit – Open-source security linter for AI agents (OWASP ASI-10)

**Body:**
> Hey HN,
> 
> We are seeing a massive shift in 2026 from single-turn chat completion bots to multi-step autonomous agents calling shell tools, executing SQL, and delegating tasks over Model Context Protocol (MCP).
> 
> Traditional AppSec (Snyk, SonarQube) checks static source code, and LLM guardrails (Llama Guard) check conversational prompts. Neither evaluates what happens when an autonomous agent is given a tool that can drop a database, run unescaped shell commands, or recursively delegate across agents.
> 
> With the OWASP Top 10 for Agentic Applications (ASI01-ASI10) published this year, we built **AgentSec Audit** to give developers an automated CI/CD security check before deploying autonomous agents:
> 
> - **Repo & Action:** https://github.com/hicklax13/agentsec-audit
> - **Live Site:** https://agentsec-audit.com
> 
> You can install the CLI locally:
> ```bash
> pip install agentsec-audit
> agentsec scan ./agent_manifest.json
> ```
> 
> Or add it as a one-liner in GitHub Actions (`uses: hicklax13/agentsec-audit@v1.0.0`) to fail PRs if dangerous arbitrary shell execution or unscoped root tokens are detected.
> 
> It also runs as an MCP server so Hermes, Claude Code, and Codex can run automated pre-commit audits on their own tool manifests.
> 
> Would love your feedback on the heuristics and false-positive handling!

---

## 2. Product Hunt Launch Brief

- **Tagline:** Automated security & compliance linter for autonomous AI agents
- **Category:** Developer Tools, Artificial Intelligence, Cybersecurity
- **Pricing:** Free developer CLI / $49/mo Team CI/CD / $249/mo Enterprise Compliance
- **First Comment:**
  > "Autonomous agents are only as safe as the tools they are handed. We built AgentSec Audit to make sure no developer accidentally ships an agent with unrestricted bash access, self-defeating safety prompts, or unscoped root keys. Run it in CLI, GitHub Actions, or over MCP."
