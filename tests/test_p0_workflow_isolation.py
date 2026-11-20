from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = {
    "daily_data": ROOT / ".github" / "workflows" / "daily_data.yml",
    "v9_pro": ROOT / ".github" / "workflows" / "daily-premarket-v9-pro.yml",
}


class P0WorkflowIsolationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflows = {
            name: path.read_text(encoding="utf-8")
            for name, path in WORKFLOWS.items()
        }

    def _trigger_block(self, name):
        workflow = self.workflows[name]
        match = re.search(
            r"(?ms)^on:\s*\n(?P<body>.*?)(?=^[A-Za-z_][A-Za-z0-9_-]*:|\Z)",
            workflow,
        )
        self.assertIsNotNone(match, f"{name} workflow has no top-level on block")
        return match.group("body")

    def test_daily_data_is_manual_dispatch_only(self):
        triggers = self._trigger_block("daily_data")
        self.assertRegex(triggers, r"(?m)^  workflow_dispatch:\s*$")
        self.assertNotRegex(triggers, r"(?m)^  (?:push|schedule|pull_request):")

    def test_v9_pro_dashboard_is_manual_dispatch_only(self):
        triggers = self._trigger_block("v9_pro")
        self.assertRegex(triggers, r"(?m)^  workflow_dispatch:\s*$")
        self.assertNotRegex(triggers, r"(?m)^  (?:push|schedule|pull_request):")

    def test_daily_data_manual_inputs_and_report_validation_are_preserved(self):
        workflow = self.workflows["daily_data"]
        self.assertIn("      t0:", workflow)
        self.assertIn("      force_rewrite:", workflow)
        self.assertIn("validate_data_report_file", workflow)
        self.assertIn("git push origin", workflow)

    def test_v9_pro_manual_date_input_and_build_checkout_are_preserved(self):
        workflow = self.workflows["v9_pro"]
        self.assertIn("      date:", workflow)
        self.assertIn("ref: ${{ github.sha }}", workflow)
        self.assertIn("actions/upload-pages-artifact@v3", workflow)
        self.assertIn("actions/deploy-pages@v4", workflow)

    def test_v9_pro_pages_deploy_remains_branch_scoped(self):
        workflow = self.workflows["v9_pro"]
        self.assertIn(
            "if: github.ref == format('refs/heads/{0}', github.event.repository.default_branch) "
            "|| github.ref == 'refs/heads/phase2-p0-data-quality' "
            "|| github.ref == 'refs/heads/phase2-p0-ui-fixes'",
            workflow,
        )


if __name__ == "__main__":
    unittest.main()
