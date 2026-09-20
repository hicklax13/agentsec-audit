# Autonomy Map: AI-Run Operations vs. Human-Required Actions

This document details every operational requirement for running **AgentSec Audit**, identifying strictly which parts are autonomously executed by AI agents and the exact human gating steps required by legal/banking infrastructure.

---

## 1. Operating Matrix

| Workflow Domain | Operational Step | Responsible Entity | Reason / Justification |
|---|---|:---:|---|
| **Core Product** | Engine coding, rule creation, bug fixing | **AI Agent** | 100% digital code and test suites. |
| **Core Product** | OWASP ASI-10 threat updates & heuristics | **AI Agent** | Continuously scrapable from CVEs, GitHub advisory, and security research. |
| **Infrastructure** | Cloud deployment (Vercel/Fly/Cloudflare) | **AI Agent** | Autonomous Git commit and CI/CD deployment via CLI. |
| **Legal / Formation** | Business entity registration (LLC / C-Corp) | **Human Required** | Legal identity, government signatures, notary requirements. |
| **Banking / KYC** | Bank account opening (Mercury / Relay) | **Human Required** | Anti-Money Laundering (AML) and federal KYC identification rules. |
| **Billing / Merchant** | Stripe merchant account verification | **Human Required** | Beneficial ownership disclosure and bank routing link. |
| **Billing / Merchant** | Pricing tier creation, webhook code, billing portal | **AI Agent** | Completely automated via Stripe API and Python SDK. |
| **Marketing & GTM** | Landing page design, copy, SEO blog posts | **AI Agent** | Static generation, Markdown authoring, asset generation. |
| **Sales & Outreach** | Lead prospecting, GitHub issue tracking, email drafting | **AI Agent** | Programmatic search and personalized email generation. |
| **Sales & Outreach** | High-stakes legal NDA/enterprise contract signing | **Human Required** | Commercial enterprise liability and legal signature authority. |
| **Customer Support** | Tier 1/2 technical debugging, scanner questions | **AI Agent** | Automated via documentation RAG and AI helpdesk webhook. |
| **Security / Custody** | Production credential secret management (API Keys) | **Human Required** | Master password / vault ownership (1Password / environment injection). |

---

## 2. Short Human Action Checklist for Connor

To take this business live with real customers and revenue, you only need to complete these 4 one-time manual steps:

- [ ] **Step 1: Stripe Setup (15 mins)**
  - Go to [stripe.com](https://stripe.com), log in/register, complete business identity verification, and link payout bank.
  - Generate a Restricted API Key with `Products: Write`, `Prices: Write`, `Checkout Sessions: Write`.
  - Put the keys in `.env` (`STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`).

- [ ] **Step 2: Domain & DNS (5 mins)**
  - Register domain (e.g., `agentsec.dev` or `agentsec-audit.com` via Cloudflare Registrar or Namecheap, ~$10/yr).
  - Point CNAME to your Vercel/Cloudflare Workers deployment.

- [ ] **Step 3: GitHub Organization / App (10 mins)**
  - Create a GitHub App or Personal Access Token under your GitHub account for the `agentsec` Action to post PR comments.

- [ ] **Step 4: Legal & Tax (Post-Revenue / <30 days)**
  - Form a single-member LLC via your state or Stripe Atlas once revenue exceeds $1,000.
