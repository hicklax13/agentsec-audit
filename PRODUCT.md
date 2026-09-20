# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

static HTML/CSS (single-file landing page, no build step), deployed via GitHub Pages.

## Users

Primary users: engineering leaders and AI engineers at B2B SaaS startups (5-250 employees) who are shipping autonomous AI agents (tool-calling, MCP-based) to production. Secondary: security engineers / DevSecOps owners and compliance leads who gate enterprise procurement.

## Product Purpose

AgentSec Audit is an open-source CLI and GitHub Action that lints AI agent configurations (system prompts, tool/function schemas, MCP server manifests) against the OWASP Top 10 for Agentic Applications (ASI01-ASI10), auto-remediates violations, and generates PDF compliance evidence (SOC 2 Type II processing integrity, ISO 42001 readiness).

## Positioning

Traditional AppSec (Snyk, SonarQube) inspects static code syntax; LLM guardrails (Llama Guard) inspect conversational text. Neither inspects the autonomous tool-execution loop. AgentSec is the security layer for the agent execution loop itself - the first audit gate between an agent config and production.

## Operating Context

Developers run `agentsec scan` locally or in GitHub Actions; agents (Hermes, Claude Code, Codex) invoke it over MCP; compliance teams consume the PDF audit packs. Distribution is GitHub Marketplace, GitHub Pages, Show HN, and Product Hunt.

## Capabilities and Constraints

- CLI: `agentsec scan` (json/html/pdf), `agentsec fix` (auto-remediation)
- MCP server mode (stdio JSON-RPC) exposing `audit_agent_config`
- GitHub Action `hicklax13/agentsec-audit@v1.0.0`
- Pricing tiers: Free Developer CLI, $49/mo Team CI/CD, $249/mo Compliance Pro (Stripe payment links embedded)
- Constraint: single static HTML file with no JavaScript build pipeline; fonts via Google Fonts; all visuals must be self-contained (CSS/SVG/inline, no external image dependencies)

## Brand Commitments

- Brand colors: Red, Black, White, Gray (explicitly requested by the principal)
- Name: "AgentSec Audit"; logo mark is a shield
- Voice: precise, technical, security-engineer-serious; no hype verbs (no "unleash", "revolutionize", "elevate")

## Evidence on Hand

- Working scanner with verified test output (10/100 failing sample, 100/100 after auto-fix)
- Live repo: https://github.com/hicklax13/agentsec-audit
- Live terminal transcript outputs from real scans (reproducible)
- No customer logos or testimonials yet; none may be fabricated

## Product Principles

1. Proof over claims: show real scanner output, real terminal sessions, real diffs
2. Security-serious: dark, precise, engineered feel; trust through craft
3. Developer-native: everything reachable from CLI, GitHub, and MCP
4. No fabricated social proof or fake-precision numbers

## Accessibility & Inclusion

WCAG AA contrast on all text; keyboard-navigable focus states; reduced-motion respect.
