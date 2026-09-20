import json

PROSPECT_EMAIL_TEMPLATE = """Subject: Quick question about security linting for {{repo_name}}

Hi {{founder_name}},

Noticed {{repo_name}} is adding tool-calling autonomous agents with access to {{notable_tool}}.

With OWASP releasing the official 2026 Top 10 for Agentic Applications (ASI01-ASI10), many engineering teams are getting hit by enterprise procurement blocks around goal hijacking and tool privilege escalation.

We built an open-source scanner (AgentSec) that lints agent configurations in CI/CD and generates automated compliance proofs for SOC 2 / ISO 42001.

Ran a quick sample pass on your open schema — would you like the 1-page HTML vulnerability and policy audit report?

Best,
Connor
Founder, AgentSec.dev
"""

SAMPLE_TARGETS = [
    {
        "repo": "crewai-examples/finance-agent",
        "lead": "Founder / AI Lead",
        "tool": "database execution & shell commands"
    },
    {
        "repo": "langchain-ai/agent-templates",
        "lead": "CTO / Eng Lead",
        "tool": "external webhooks & API credentials"
    }
]

if __name__ == "__main__":
    print("Generating sample outreach queue...")
    for target in SAMPLE_TARGETS:
        rendered = PROSPECT_EMAIL_TEMPLATE.replace("{{repo_name}}", target["repo"]).replace("{{founder_name}}", target["lead"]).replace("{{notable_tool}}", target["tool"])
        print("\n" + "="*40)
        print(rendered)
