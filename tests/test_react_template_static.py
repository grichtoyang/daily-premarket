from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "v9-pro-react-template.html"


class ReactTemplateStaticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = TEMPLATE.read_text(encoding="utf-8")

    def test_template_uses_injected_dashboard_data_without_demo_fallback(self):
        self.assertIn("var vf=window.DASHBOARD_DATA;", self.html)
        self.assertNotIn("window.DASHBOARD_DATA||df", self.html)
        self.assertNotIn("var vf=df", self.html)
        for binding in ("l.factor_details", "l.instOptForce", "n.top10Call", "n.top10Put"):
            self.assertIn(binding, self.html)

    def test_known_hardcoded_market_samples_are_absent(self):
        forbidden = (
            "-86043", "85052", "48600", "1972口", "48500", "53500", "47000",
            "-1742", "-1854", "-3596", "13.85", "13.88", "5.41", "5.28",
            "-0.03", "+0.12", "+1451", "-1794", "+296", "+1470", "-4736",
            "+976", "開高續漲 70%", "悲觀30%", "中性40%", "樂觀30%",
            "SOX+3.6%", "ADR+1.4%", "Bias44分", "10Y近5%", "VIX -4.73%",
            "WTI-1.34%", "BTC+0.77%", "新聞10則", "重大新聞 8則",
            "90天飆498%", "509億", "破46K",
        )
        present = [value for value in forbidden if value in self.html]
        self.assertEqual(present, [], f"Hardcoded sample data remains: {present}")

    def test_factor_and_chart_values_are_not_hardcoded(self):
        self.assertIsNone(
            re.search(r"\bv\s*:\s*[-+]?\d+(?:\.\d+)?", self.html),
            "Numeric chart data literals must come from DATA_REPORT/Builder JSON",
        )

    def test_inline_javascript_syntax(self):
        node = shutil.which("node")
        self.assertIsNotNone(node, "Node.js is required for React template syntax validation")
        scripts = re.findall(r"<script\b([^>]*)>([\s\S]*?)</script\s*>", self.html, re.IGNORECASE)
        checked = 0
        with tempfile.TemporaryDirectory() as tmp:
            for index, (attrs, source) in enumerate(scripts):
                if "application/json" in attrs.lower() or not source.strip():
                    continue
                suffix = ".mjs" if 'type="module"' in attrs.lower() else ".js"
                path = Path(tmp) / f"inline_{index}{suffix}"
                path.write_text(source, encoding="utf-8")
                result = subprocess.run(
                    [node, "--check", str(path)],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                diagnostic = ""
                if result.returncode:
                    error_lines = result.stderr.splitlines()
                    for line_index, error_line in enumerate(error_lines):
                        match = re.search(rf"{re.escape(path.name)}:(\d+)", error_line)
                        if match:
                            source_line = error_lines[line_index + 1] if line_index + 1 < len(error_lines) else ""
                            caret_line = error_lines[line_index + 2] if line_index + 2 < len(error_lines) else ""
                            column = caret_line.find("^")
                            context = source_line[max(0, column - 100):column + 100] if column >= 0 else source_line[-200:]
                            diagnostic = f"{error_line}; column={column}; context={context}; message={error_lines[-1] if error_lines else ''}"
                            break
                    if not diagnostic:
                        diagnostic = "\n".join(error_lines[-3:])
                self.assertEqual(
                    result.returncode,
                    0,
                    f"JavaScript syntax error in inline script {index}:\n{diagnostic}",
                )
                checked += 1
        self.assertGreater(checked, 0, "No inline JavaScript was checked")


if __name__ == "__main__":
    unittest.main()
