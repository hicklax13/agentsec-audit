import argparse
import json
import sys
import os
from .scanner import AgentScanner

def generate_html_report(report_data: dict) -> str:
    issues_html = ""
    for issue in report_data.get("issues", []):
        badge_color = "#dc2626" if issue["severity"] == "CRITICAL" else "#ea580c" if issue["severity"] == "HIGH" else "#ca8a04"
        issues_html += f"""
        <div style="border: 1px solid #334155; border-radius: 8px; padding: 16px; margin-bottom: 12px; background: #1e293b;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-weight: bold; font-size: 1.1em; color: #f8fafc;">[{issue['code']}] {issue['title']}</span>
                <span style="background: {badge_color}; color: white; padding: 4px 10px; border-radius: 9999px; font-size: 0.75em; font-weight: bold;">{issue['severity']}</span>
            </div>
            <p style="color: #cbd5e1; margin: 4px 0;"><strong>Finding:</strong> {issue['description']}</p>
            <p style="color: #38bdf8; margin: 4px 0;"><strong>Fix:</strong> {issue['remediation']}</p>
        </div>
        """

    status_color = "#16a34a" if report_data["status"] == "PASSED" else "#dc2626"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AgentSec Audit Report - {report_data.get('target')}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0f172a; color: #f8fafc; padding: 32px; margin: 0; }}
        .container {{ max-width: 800px; margin: 0 auto; }}
        .header {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #334155; padding-bottom: 20px; }}
        .badge {{ background: {status_color}; color: white; padding: 8px 16px; border-radius: 6px; font-weight: bold; font-size: 1.1em; }}
        .score {{ font-size: 3em; font-weight: 800; color: {status_color}; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div>
                <h1 style="margin: 0; font-size: 1.8em;">AgentSec Audit Report</h1>
                <p style="margin: 4px 0; color: #94a3b8;">Target: <strong>{report_data.get('target')}</strong> | Framework: OWASP ASI-10 (2026)</p>
            </div>
            <div class="badge">{report_data.get('status')}</div>
        </div>

        <div style="display: flex; gap: 24px; margin: 24px 0;">
            <div style="flex: 1; background: #1e293b; padding: 20px; border-radius: 8px; text-align: center;">
                <div style="color: #94a3b8; font-size: 0.9em;">Security Rating</div>
                <div class="score">{report_data.get('security_score')}/100</div>
            </div>
            <div style="flex: 1; background: #1e293b; padding: 20px; border-radius: 8px; text-align: center;">
                <div style="color: #94a3b8; font-size: 0.9em;">Violations Detected</div>
                <div style="font-size: 3em; font-weight: 800; color: #f8fafc;">{report_data.get('issue_count')}</div>
            </div>
        </div>

        <h3>Vulnerability & Policy Findings</h3>
        {issues_html if issues_html else "<p style='color: #4ade80;'>Zero vulnerabilities found. Full OWASP ASI-10 compliance achieved.</p>"}
    </div>
</body>
</html>
"""

def main():
    parser = argparse.ArgumentParser(description="AgentSec Audit CLI - Automated AI Agent Security & Compliance Linter")
    subparsers = parser.add_subparsers(dest="command")

    scan_parser = subparsers.add_parser("scan", help="Scan an agent specification or tool config file")
    scan_parser.add_argument("file", help="Path to JSON/YAML agent config file")
    scan_parser.add_argument("--format", choices=["json", "html", "pdf"], default="json", help="Output format")
    scan_parser.add_argument("--out", help="Output file path (optional)")

    fix_parser = subparsers.add_parser("fix", help="Automatically patch and remediate detected security violations")
    fix_parser.add_argument("file", help="Path to JSON/YAML agent config file")
    fix_parser.add_argument("--out", help="Output file path (overwrites in-place if omitted)")

    args = parser.parse_args()

    if args.command == "scan":
        if not os.path.exists(args.file):
            print(f"Error: Target file '{args.file}' not found.", file=sys.stderr)
            sys.exit(1)

        with open(args.file, "r", encoding="utf-8") as f:
            try:
                config_data = json.load(f)
            except Exception as e:
                print(f"Error parsing JSON file: {e}", file=sys.stderr)
                sys.exit(1)

        scanner = AgentScanner()
        results = scanner.scan_config(config_data)

        if args.format == "html":
            output = generate_html_report(results)
        elif args.format == "pdf":
            import subprocess
            out_pdf = args.out if args.out else "audit-report.pdf"
            temp_html = "temp_audit_report.html"
            with open(temp_html, "w", encoding="utf-8") as f:
                f.write(generate_html_report(results))
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            subprocess.run([chrome_path, "--headless", "--disable-gpu", f"--print-to-pdf={out_pdf}", temp_html], check=True)
            if os.path.exists(temp_html):
                os.remove(temp_html)
            print(f"Compliance PDF successfully generated at {out_pdf}")
            sys.exit(0 if results["status"] == "PASSED" else 2)
        else:
            output = json.dumps(results, indent=2)

        if args.out:
            with open(args.out, "w", encoding="utf-8") as f:
                f.write(output)
            print(f"Audit report successfully exported to {args.out}")
        else:
            print(output)

        if results["status"] != "PASSED":
            sys.exit(2)
    elif args.command == "fix":
        if not os.path.exists(args.file):
            print(f"Error: Target file '{args.file}' not found.", file=sys.stderr)
            sys.exit(1)

        with open(args.file, "r", encoding="utf-8") as f:
            try:
                config_data = json.load(f)
            except Exception as e:
                print(f"Error parsing JSON file: {e}", file=sys.stderr)
                sys.exit(1)

        from .patcher import AgentPatcher
        patcher = AgentPatcher()
        patched_data, fixes = patcher.patch_config(config_data)

        out_path = args.out if args.out else args.file
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(patched_data, f, indent=2)

        print(f"\n[AgentSec Auto-Remediation] Successfully patched '{out_path}':")
        if fixes:
            for fix in fixes:
                print(f"  ✓ {fix}")
        else:
            print("  (No fixable violations detected)")
        print(f"\nVerification: Run `agentsec scan {out_path}` to confirm full compliance.\n")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
