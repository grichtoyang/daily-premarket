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
        scripts = "\n".join(
            source for attrs, source in re.findall(
                r"<script\b([^>]*)>([\s\S]*?)</script\s*>", self.html, re.IGNORECASE
            )
            if "application/json" not in attrs.lower()
        )
        data_fields = (
            "v", "value", "score", "bias", "price", "close", "open", "high", "low",
            "change", "pct", "percent", "ratio", "volume", "oi", "pcr", "rsi", "macd",
            "strike", "wall", "flip", "maxPain", "callWall", "putWall", "gammaWall",
            "count", "weight", "amount", "total", "net", "up", "down", "flat",
            "timestamp", "year", "month", "day", "x", "y",
        )
        fields = "|".join(re.escape(field) for field in data_fields)
        object_literals = re.findall(
            rf"\b(?:{fields})\s*:\s*[+-]?\d+(?:\.\d+)?\b",
            scripts,
            re.IGNORECASE,
        )
        self.assertEqual(
            object_literals,
            [],
            "Numeric market-data properties must come from DATA_REPORT/Builder JSON",
        )
        literal_arrays = re.findall(
            r"\b(?:data|series|values|points)\s*:\s*\[\s*[+-]?\d+(?:\.\d+)?",
            scripts,
            re.IGNORECASE,
        )
        self.assertEqual(
            literal_arrays,
            [],
            "Chart data arrays must be derived from injected dashboard data",
        )
        declared_numeric_arrays = re.findall(
            r"\b(?:const|let|var)\s+[A-Za-z_$][\w$]*\s*=\s*\[\s*[+-]?\d+(?:\.\d+)?",
            scripts,
        )
        self.assertEqual(
            declared_numeric_arrays,
            [],
            "Standalone numeric sample arrays are not allowed in the React template",
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
