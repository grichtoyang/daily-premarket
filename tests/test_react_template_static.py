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

    def test_pre_change_template_stages_parse(self):
        node = shutil.which("node")
        self.assertIsNotNone(node)
        parser = "const fs=require('fs');const acorn=require('acorn');try{acorn.parse(fs.readFileSync(process.argv[1],'utf8'),{ecmaVersion:'latest',sourceType:'module'});}catch(e){console.error(e.message+' at '+(e.loc?e.loc.line+':'+e.loc.column:''));process.exit(1)}"
        baseline_shas = (
            "10a1b50848a375436c47efa0e6878dbddccce67b",
            "521676a467fc84b1d9ee8ea83c33332499d8f018",
        )
        with tempfile.TemporaryDirectory() as tmp:
            for baseline_sha in baseline_shas:
                fetch = subprocess.run(["git", "fetch", "--no-tags", "--depth=1", "origin", baseline_sha], capture_output=True, text=True, check=False)
                self.assertEqual(fetch.returncode, 0, fetch.stderr[-1000:])
                baseline = subprocess.run(["git", "show", f"{baseline_sha}:templates/v9-pro-react-template.html"], capture_output=True, text=True, check=False)
                self.assertEqual(baseline.returncode, 0, baseline.stderr[-1000:])
                scripts = re.findall(r"<script\\b([^>]*)>([\\s\\S]*?)</script\\s*>", baseline.stdout, re.IGNORECASE)
                for index, (attrs, source) in enumerate(scripts):
                    if "application/json" in attrs.lower() or not source.strip():
                        continue
                    path = Path(tmp) / f"baseline_{baseline_sha[:6]}_{index}.mjs"
                    path.write_text(source, encoding="utf-8")
                    result = subprocess.run([node, "-e", parser, str(path)], capture_output=True, text=True, check=False)
                    self.assertEqual(result.returncode, 0, f"Baseline {baseline_sha[:6]} script {index}: {result.stderr.strip()}")

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
                parser = "const fs=require('fs');const acorn=require('acorn');try{acorn.parse(fs.readFileSync(process.argv[1],'utf8'),{ecmaVersion:'latest',sourceType:'module'});}catch(e){console.error(e.message+' at '+(e.loc?e.loc.line+':'+e.loc.column:''));process.exit(1)}"
                result = subprocess.run(
                    [node, "-e", parser, str(path)],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                diagnostic = result.stderr.strip()
                self.assertEqual(
                    result.returncode,
                    0,
                    f"JavaScript syntax error in inline script {index}:\n{diagnostic}",
                )
                checked += 1
        self.assertGreater(checked, 0, "No inline JavaScript was checked")


if __name__ == "__main__":
    unittest.main()
