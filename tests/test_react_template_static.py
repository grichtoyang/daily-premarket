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

    def test_borrowed_securities_fields_and_scope_are_rendered(self):
        for field in ("borrowedSell", "borrowedSellDiff", "borrowedSellDiffScope"):
            self.assertIn(field, self.html)
        self.assertIn("借券賣出增減｜", self.html)
        self.assertIn('function qn(e,n){kr(e,n),kr(e+"Capture",n)}', self.html)

    def test_borrowed_securities_table_stacks_on_mobile_without_wrapping_values(self):
        self.assertIn('className:"borrowed-sbl-table"', self.html)
        self.assertIn(".borrowed-sbl-table { grid-template-columns: minmax(0, 1fr); }", self.html)
        self.assertIn(".borrowed-sbl-table > div > span:last-child { flex-shrink: 0; white-space: nowrap; }", self.html)

    def test_option_institutional_chart_parses_signed_thousands(self):
        # The chart must render both session fields, not just the daytime field.
        self.assertIn('{l:String(x[0])+"日",v:v9ProOptionNetNumber(x[3]),extra:"日"}', self.html)
        self.assertIn('{l:String(x[0])+"夜",v:v9ProOptionNetNumber(x[6]),extra:"夜"}', self.html)
        self.assertIn('height:390}),table:p("div",{className:"text-[10px] mono space-y-1"', self.html)
        self.assertIn(".filter((item)=>Number.isFinite(item.v))", self.html)
        match = re.search(r"function v9ProOptionNetNumber\(e\)\{[^}]+\}", self.html)
        self.assertIsNotNone(match, "Chart number normalizer v9ProOptionNetNumber must exist")
        node = shutil.which("node")
        self.assertIsNotNone(node, "Node.js is required for chart number parsing tests")
        script = (
            match.group(0)
            + ';const actual=[v9ProOptionNetNumber("+6,624"),v9ProOptionNetNumber("-4,937"),v9ProOptionNetNumber("0"),v9ProOptionNetNumber(null),v9ProOptionNetNumber(""),v9ProOptionNetNumber("not-a-number")];'
            + 'const expected=[6624,-4937,0,null,null,null];'
            + 'if(JSON.stringify(actual)!==JSON.stringify(expected)){console.error(actual);process.exit(1)}'
        )
        result = subprocess.run([node, "-e", script], capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_option_pcr_card_shows_call_put_volume_structure(self):
        self.assertIn('function yf({callVol:e,putVol:n,height:l=200})', self.html)
        self.assertIn('title:"PCR／成交量結構"', self.html)
        self.assertIn('chart:p(yf,{callVol:n.callVol,putVol:n.putVol,height:200})', self.html)
        self.assertIn('Call／Put 成交量占比（合計 100%）', self.html)
        self.assertIn('Put 成交量', self.html)
        self.assertIn('成交量只呈現 Call／Put 相對結構，不直接代表多空方向', self.html)
        self.assertIn('Call OI', self.html)
        self.assertIn('Put OI', self.html)
        self.assertIn('PCR 是 Put／Call 比值；成交量反映當日交易活躍度，OI 反映未平倉部位', self.html)
        self.assertIn('PCR ${B(n.pcr,2)}；成交量與 OI 分開觀察', self.html)
        self.assertNotIn('title:"Call/Put Vol OI PCR"', self.html)
        self.assertNotIn('label:`上市 ${g(e)}億', self.html)
        self.assertNotIn('label:`上櫃 ${g(n)}億', self.html)

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


    def test_three_scenario_paths_render_conditionally_without_probability_or_maxpain_target(self):
        self.assertIn('function Pth({current:e,levels:n})', self.html)
        self.assertIn('chart:p(Pth,{current:i.close,levels:{putWall:l.putWall,callWall:l.callWall,gammaWall:l.gammaWall,flip:l.flip}})', self.html)
        self.assertIn('情境一｜偏多', self.html)
        self.assertIn('情境二｜區間', self.html)
        self.assertIn('情境三｜偏空', self.html)
        self.assertIn('d.id==="range"?(x.k==="putWall"?"位於":"↔"):"→"', self.html)
        self.assertIn('MaxPain 僅作磁吸參考，不當作跌破後的下跌目標', self.html)
        self.assertIn('缺少位於現價正確方向的有效關鍵價位，暫不繪製延伸路徑', self.html)
        self.assertNotIn('"加速至$",g(l.maxPain)', self.html)

    def test_kpi_sparklines_do_not_fabricate_history(self):
        self.assertIn("function e2(e,n=10,r=0.02,l=0){return[]}", self.html)

    def test_market_index_renderer_exists_without_fabricated_sparkline(self):
        self.assertIn("function gf({data:e,height:n=220})", self.html)
        self.assertIn('走勢(無資料)', self.html)
        self.assertIn('F+f/2,k+t/2+1', self.html)
        self.assertNotIn("(Math.random()-0.5)*0.6", self.html)
    def test_financing_gauge_uses_dynamic_range(self):
        self.assertIn(
            "F=Math.max(0,Math.floor((e-1000)/1000)*1000),a=F+2000,v=(e-F)/(a-F)",
            self.html,
        )
        self.assertNotIn("F=7000,a=9000", self.html)

    def test_futures_volume_bar_is_capped_to_available_height(self):
        self.assertIn("Math.min(1,o/Math.max(200000,o))*20", self.html)
        self.assertNotIn("o/200000*22", self.html)

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
