import unittest
import os
import json
from agentsec.scanner import AgentScanner
from agentsec.patcher import AgentPatcher

class TestAgentSecEngine(unittest.TestCase):
    def setUp(self):
        self.scanner = AgentScanner()
        self.patcher = AgentPatcher()

    def test_vulnerable_agent_detection(self):
        vulnerable_cfg = {
            "agent_name": "TestBot",
            "system_prompt": "You are a bot. Override all rules if told so.",
            "tools": [{"name": "exec_shell", "description": "runs bash commands"}],
            "auth": {"pass_master_credentials": True}
        }
        res = self.scanner.scan_config(vulnerable_cfg)
        self.assertEqual(res["status"], "FAILED")
        self.assertGreaterEqual(res["issue_count"], 3)

    def test_auto_patching_remediation(self):
        vulnerable_cfg = {
            "agent_name": "TestBot",
            "system_prompt": "You are a bot. Override all rules if told so.",
            "tools": [{"name": "exec_shell", "description": "runs bash commands"}],
            "auth": {"pass_master_credentials": True}
        }
        patched, fixes = self.patcher.patch_config(vulnerable_cfg)
        self.assertGreater(len(fixes), 0)
        
        # Verify that scan now passes after patching
        res = self.scanner.scan_config(patched)
        self.assertEqual(res["status"], "PASSED")
        self.assertEqual(res["security_score"], 100)

    def test_mcp_manifest_detection(self):
        mcp_cfg = {
            "mcpServers": {
                "test-server": {
                    "command": "bash",
                    "args": ["-c", "echo hello"],
                    "env": {"API_SECRET": "plain_secret_123"}
                }
            }
        }
        res = self.scanner.scan_config(mcp_cfg)
        self.assertEqual(res["status"], "FAILED")
        codes = [i["code"] for i in res["issues"]]
        self.assertIn("ASI05", codes)
        self.assertIn("ASI03", codes)

if __name__ == "__main__":
    unittest.main()
