from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "daily-premarket-v9-pro.yml"
INTEGRATION = ROOT / ".github" / "workflows" / "test-data-report-margin-ratio.yml"


class P0WorkflowIsolationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = WORKFLOW.read_text(encoding="utf-8")
        cls.integration = INTEGRATION.read_text(encoding="utf-8")

    def test_manual_dispatch_and_explicit_master_p0_push_triggers(self):
        self.assertIn("workflow_dispatch:", self.workflow)
        push_section = self.workflow.split("  schedule:", 1)[0]
        self.assertRegex(push_section, r"(?ms)^  push:\s*branches:\s*\n\s+- master(?:\s|$)")
        self.assertIn("- phase2-p0-data-quality", push_section)

    def test_checkout_and_generated_commit_are_explicitly_p0_scoped(self):
        self.assertIn("ref: ${{ github.ref }}", self.workflow)
        self.assertIn("if: github.ref == 'refs/heads/phase2-p0-data-quality'", self.workflow)
        self.assertIn('${GITHUB_REF_NAME}" != "phase2-p0-data-quality"', self.workflow)
        self.assertIn('git push origin "HEAD:${GITHUB_REF_NAME}"', self.workflow)
        self.assertNotRegex(self.workflow, r"(?m)^\s*git push\s*$")
        self.assertIn("git add dashboards/", self.workflow)
        self.assertNotIn("git add data_reports", self.workflow)

    def test_pages_deploy_is_restricted_to_default_branch(self):
        self.assertIn("if: github.ref == format('refs/heads/{0}', github.event.repository.default_branch)", self.workflow)
        self.assertIn("uses: actions/deploy-pages@v4", self.workflow)

    def test_p0_integration_workflow_cannot_deploy_pages(self):
        self.assertIn("permissions:\n  contents: read", self.integration)
        self.assertNotIn("actions/deploy-pages@", self.integration)
        self.assertNotRegex(self.integration, r"(?m)^\s+deploy:")


if __name__ == "__main__":
    unittest.main()
