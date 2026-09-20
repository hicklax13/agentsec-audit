"""
FastMCP Server for AgentSec Audit
Exposes the agent security audit engine directly over Model Context Protocol (MCP)
so Hermes Desktop, Claude Code, and Codex can invoke it as a native tool.
"""

import sys
import json
from .scanner import AgentScanner

def handle_request(req_str: str) -> str:
    try:
        req = json.loads(req_str)
    except Exception as e:
        return json.dumps({"error": f"Invalid JSON: {str(e)}"})

    method = req.get("method")
    scanner = AgentScanner()

    if method == "tools/list":
        return json.dumps({
            "tools": [
                {
                    "name": "audit_agent_config",
                    "description": "Lints an AI agent configuration, prompt, and tool manifest against OWASP Top 10 for Agentic Applications (ASI01-ASI10) and SOC 2 / ISO 42001 compliance standards.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "agent_config": {
                                "type": "object",
                                "description": "The JSON agent configuration containing system_prompt, tools, auth, memory, and delegation parameters."
                            }
                        },
                        "required": ["agent_config"]
                    }
                }
            ]
        })

    elif method == "tools/call":
        params = req.get("params", {})
        name = params.get("name")
        arguments = params.get("arguments", {})

        if name == "audit_agent_config":
            config = arguments.get("agent_config", {})
            report = scanner.scan_config(config)
            return json.dumps({
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps(report, indent=2)
                    }
                ]
            })
        else:
            return json.dumps({"error": f"Unknown tool '{name}'"})

    return json.dumps({"error": f"Unsupported method '{method}'"})

def main():
    # Stdio loop for MCP JSON-RPC protocol
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        res = handle_request(line)
        sys.stdout.write(res + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
