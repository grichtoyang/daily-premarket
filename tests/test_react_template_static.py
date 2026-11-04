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
        self.assertIn('{l:String(x[0])+"日",v:v9ProOptionNetNumber(x[3]),extra:"口"}', self.html)
        self.assertIn('{l:String(x[0])+"夜",v:v9ProOptionNetNumber(x[6]),extra:"口"}', self.html)
        self.assertIn('height:390}),chartNote:"法人日盤／夜盤淨交易：口；依來源表格定義。"', self.html)
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

    def test_candlestick_volume_unit_is_not_shadowed_by_canvas_coordinate(self):
        # The candle x-coordinate must not overwrite the unit label passed by the chart caller.
        self.assertIn('volUnit:unitLabel="口"', self.html)
        self.assertIn('s.fillText(`VOL ${g(o)}${unitLabel}`,S+Ee+10,A+11)', self.html)
        self.assertNotIn('volUnit:a="口"', self.html)
        self.assertNotIn('s.fillText(`VOL ${g(o)}${a}`,S+Ee+10,A+11)', self.html)

    def test_all_three_ranked_charts_expand_without_container_clipping(self):
        # Hn is shared by the futures day/night institutional chart, options top-10 chart,
        # and per-strike GEX chart. Its canvas must grow to fit every rendered row.
        self.assertIn("height:Math.max(n,e.length*46+48)", self.html)
        self.assertIn('style:{minHeight:"180px"}', self.html)
        self.assertIn('className:"bg-[#0a1424]"', self.html)
        self.assertIn('style:{width:"100%",height:Math.max(n,e.length*46+48),display:"block",maxWidth:"100%"}', self.html)
        self.assertIn('title:"日夜法人交易"', self.html)
        self.assertIn('height:220}),chartNote:"未平倉量與日／夜盤淨交易均為口數，統計意義不同。', self.html)
        self.assertIn('title:"前十大選擇權"', self.html)
        self.assertIn("(n.top10Call||[]).slice(0,3)", self.html)
        self.assertIn("(n.top10Put||[]).slice(0,3)", self.html)
        self.assertIn('title:"履約價 GEX 分布"', self.html)
        self.assertIn(".sort((a,b)=>Math.abs(b.v)-Math.abs(a.v)).slice(0,16)", self.html)
        self.assertIn('chartNote:"GEX：新台幣元（NT$）', self.html)
        self.assertIn('height:260}),chartNote:"GEX：新台幣元', self.html)

    def test_bias_card_renders_live_gex_status_and_value(self):
        self.assertIn('gexReady=l.gexStatus==="available"&&Number.isFinite(gexValue)', self.html)
        self.assertIn('gexLabel=gexReady?', self.html)
        self.assertIn('toFixed(2)', self.html)
        self.assertIn("gexValue/1e8", self.html)
        self.assertIn("億 NT$", self.html)
        self.assertIn('{label:gexLabel,color:gexColor', self.html)
        self.assertIn('gexLabel," · MaxPain "', self.html)
        self.assertNotIn('label:"GEX unavailable"', self.html)
        self.assertNotIn('" · GEX unavailable · MaxPain "', self.html)

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
        self.assertIn('OI PCR ${B(n.pcr,2)}倍；成交量與 OI 分開觀察', self.html)
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
        self.assertIn('const rangeReady = cur != null && put != null && call != null && put < cur && cur < call', self.html)
        self.assertIn('complete:cur != null && flip != null && cur > flip && bullTargets.length > 0', self.html)
        self.assertIn('complete:cur != null && put != null && cur < put && bearTargets.length > 0', self.html)
        self.assertIn('站穩／有效跌破仍須後續價格行為確認', self.html)
        self.assertIn('MaxPain 僅作磁吸參考，不當作跌破後的下跌目標', self.html)

    def test_kpi_sparklines_do_not_fabricate_history(self):
        self.assertIn("function e2(e,n=10,r=0.02,l=0){return[]}", self.html)

    def test_market_index_renderer_exists_without_fabricated_sparkline(self):
        self.assertIn('function gf({data:e,height:n=220,changeUnit:unit="%"})', self.html)
        self.assertIn('走勢(無資料)', self.html)
        self.assertIn('F+f/2,k+t/2+1', self.html)
        self.assertNotIn("(Math.random()-0.5)*0.6", self.html)

    def test_financing_gauge_uses_dynamic_range(self):
        self.assertIn("validFinance=e!=null&&Number.isFinite(Number(e))", self.html)
        self.assertIn("validRatio=l!=null&&Number.isFinite(Number(l))", self.html)
        self.assertIn("if(validFinance){let F=Math.max(0,Math.floor((Number(e)-1000)/1000)*1000)", self.html)
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
                # Node's built-in parser is sufficient here; do not depend on undeclared acorn.
                result = subprocess.run(
                    [node, "--check", str(path)],
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

    def test_bias_chart_uses_signed_factor_contributions_and_chinese_names(self):
        self.assertIn('title:"多空因子方向貢獻"', self.html)
        self.assertIn("Bias ${u.bias}分｜${u.regime}", self.html)
        self.assertIn('(u.factor_details||[]).filter(x=>x.status==="active"&&Number.isFinite(Number(x.contribution)))', self.html)
        self.assertIn('map(x=>({l:x.name,v:Number(x.contribution)}))', self.html)
        self.assertIn("方向貢獻分數（非權重）", self.html)
        self.assertIn('height:260}),chartNote:"方向貢獻分數', self.html)  # 8 rows need >=242px at current row pitch
        self.assertIn("正值推升 Bias、偏多；負值壓低 Bias、偏空", self.html)
        self.assertNotIn('Object.entries(u.weights).slice(0,8)', self.html)

    def test_option_force_table_normalizes_amounts_and_signed_net_values(self):
        self.assertIn('cellIndex===3||cellIndex===6', self.html)
        self.assertIn('numeric.toFixed(2)', self.html)
        self.assertIn('numeric>0?"+":""', self.html)
        self.assertIn('Number(String(cell).replace(/,/g,""))', self.html)
        self.assertIn("各欄由原始千元金額獨立換算並四捨五入至小數二位", self.html)
        self.assertIn("淨額以未四捨五入原始值計算", self.html)

    def test_three_scenario_runtime_paths_require_trigger_and_target_levels(self):
        start = self.html.index("function Pth(")
        end = self.html.index("function ", start + 1)
        function_source = self.html[start:end]
        node = shutil.which("node")
        self.assertIsNotNone(node, "Node.js is required for scenario path tests")
        script = """
const O=(type,props)=>({type,props});
const p=(type,props)=>({type,props});
const g=(value)=>String(value);
""" + function_source + """
function textOf(value){
  if(value==null) return "";
  if(typeof value==="string"||typeof value==="number") return String(value);
  if(Array.isArray(value)) return value.map(textOf).join(" ");
  return textOf(value.props?.children);
}
function cards(current,levels){
  const root=Pth({current,levels});
  return root.props.children.slice(1).map(x=>textOf(x).replace(/\\s+/g," "));
}
const bull=cards(110,{flip:100,gammaWall:120,callWall:130,putWall:90});
if(!bull[0].includes("現價高於 Gamma Flip 100")||!bull[0].includes("Gamma Wall 120")||!bull[0].includes("Call Wall 130")) throw Error("valid bullish path missing trigger/targets: "+bull[0]);
const bullNoFlip=cards(110,{flip:null,gammaWall:120,callWall:130});
if(!bullNoFlip[0].includes("偏多條件未成立")||bullNoFlip[0].includes("現價 110")) throw Error("bullish path rendered without Gamma Flip: "+bullNoFlip[0]);
const range=cards(100,{putWall:90,callWall:110});
if(!range[1].includes("現價位於 Put Wall 90 與 Call Wall 110 之間")||!range[1].includes("現價 100")) throw Error("valid range path missing both walls: "+range[1]);
const rangeInvalid=cards(120,{putWall:90,callWall:110});
if(!rangeInvalid[1].includes("區間條件未成立")||rangeInvalid[1].includes("現價 120")) throw Error("range path rendered when current is outside walls: "+rangeInvalid[1]);
const bear=cards(90,{putWall:100,gammaWall:80,flip:70});
if(!bear[2].includes("現價低於 Put Wall 100")||!bear[2].includes("Gamma Wall 80")||!bear[2].includes("Gamma Flip 70")) throw Error("valid bearish path missing trigger/targets: "+bear[2]);
const bearNoPut=cards(90,{putWall:null,gammaWall:80,flip:70});
if(!bearNoPut[2].includes("偏空條件未成立")||bearNoPut[2].includes("現價 90")) throw Error("bearish path rendered without Put Wall trigger: "+bearNoPut[2]);
console.log("scenario paths 6/6 PASS");
"""
        result = subprocess.run([node, "-e", script], capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("scenario paths 6/6 PASS", result.stdout)

    def test_synthesis_narratives_are_derived_from_live_data(self):
        self.assertIn("function v9ProSynthesisAnalysis({day,night,futures,spot,options,analysis})", self.html)
        self.assertIn('function v2({data:e}){let{tx:n,futures:r}=e;const narrative=v9ProSynthesisAnalysis({day:n.day,night:n.night,futures:r,spot:e.spot,options:e.options,analysis:e.analysis});', self.html)
        for binding in (
            "analysis:narrative.night", "analysis:narrative.scenarios",
            "analysis:narrative.factors", "analysis:narrative.correlation",
            "analysis:narrative.trade",
        ):
            self.assertIn(binding, self.html)
        self.assertNotIn("站上${g(l.gammaWall)}偏多，跌破${g(l.putWall)}追空", self.html)
        helper_start = self.html.index("function v9ProCorrelationMatrixReady(")
        start = self.html.index("function v9ProSynthesisAnalysis(", helper_start)
        end = self.html.index("function y2(", start)
        function_source = self.html[helper_start:end]
        self.assertIn("v9ProCorrelationMatrixReady(e.analysis.correlation?.labels,e.analysis.correlation?.matrix)", self.html)
        node = shutil.which("node")
        self.assertIsNotNone(node, "Node.js is required for synthesis narrative runtime tests")
        fixture = {
            "day": {"c": 45301, "vol": 73987},
            "night": {"c": 44433, "vol": 44305, "l": 44200},
            "futures": {"foreign_night": 1365, "foreign_oi": 0},
            "spot": {"close": 44920},
            "options": {"putWall": 44000, "callWall": 48000, "gammaWall": None, "flip": None},
            "analysis": {
                "bias": 24, "regime": "偏空",
                "factor_quality": {"active_count": 14, "confidence": "high", "missing_factors": ["gex", "yield"]},
                "factor_details": [
                    {"key":"spot_trend","name":"現貨趨勢","status":"active","contribution":-1.9},
                    {"key":"foreign_spot","name":"外資現貨","status":"active","contribution":-7.1},
                    {"key":"trust","name":"投信","status":"active","contribution":1.8},
                    {"key":"gex","name":"GEX","status":"disabled","contribution":0},
                    {"key":"yield","name":"殖利率","status":"disabled","contribution":0},
                ],
                "correlation": {
                    "labels": ["現貨","外資現貨","費半"],
                    "matrix": [[1,0.85,-0.64],[0.85,1,-0.46],[-0.64,-0.46,1]],
                    "desc": "日期對齊樣本矩陣"
                }
            }
        }
        script = "const fixture=" + __import__("json").dumps(fixture, ensure_ascii=False) + ";\n" + function_source + """
const out=v9ProSynthesisAnalysis(fixture);
if(!out.night.compass.includes("背離")) throw Error("night flow/price divergence not identified");
if(!out.scenarios.compass.includes("區間條件：成立")||!out.scenarios.compass.includes("偏多價格條件：未成立")) throw Error("scenario status not derived from levels");
if(!out.factors.look.includes("正向貢獻合計 +1.8 分")||!out.factors.look.includes("負向貢獻合計 -9.0 分")||!out.factors.look.includes("可見項目淨貢獻 -7.2 分")||!out.factors.look.includes("外資現貨 -7.1")) throw Error("visible factor contribution summary does not match chart values");
if(!out.factors.compass.includes("不可將可見子集合計當成全部 17 因子的總貢獻")) throw Error("visible factor subset limitation missing");
if(!out.correlation.look.includes("現貨／外資現貨 +0.85")||!out.correlation.look.includes("現貨／費半 -0.64")) throw Error("strongest correlation pairs not identified");
if(!out.trade.target.includes("區間內不追價")) throw Error("trade plan does not respect current range");

// Missing night price inputs must not produce actionable text containing fake zero/missing levels.
const missing=v9ProSynthesisAnalysis({day:{},night:{},futures:{},spot:{},options:{},analysis:{}});
if(!missing.night.target.includes("缺值／無效")||!missing.night.target.includes("暫不提供價位觸發條件")) throw Error("missing night price levels still produce a trigger");
if(!missing.scenarios.compass.includes("資料不足")||!missing.trade.target.includes("先補齊有效關鍵位")) throw Error("missing key levels produce a directional trade plan");

// The price-action target must reverse with night-session direction, not remain bearish.
const upNight=JSON.parse(JSON.stringify(fixture));
upNight.night.c=45500; upNight.night.l=45000; upNight.futures.foreign_night=-1200;
const upNightOut=v9ProSynthesisAnalysis(upNight);
if(!upNightOut.night.target.includes("夜盤偏強訊號")||upNightOut.night.target.includes("夜盤弱勢才獲得")) throw Error("positive night move still receives bearish target wording");
const downNight=JSON.parse(JSON.stringify(fixture));
downNight.night.c=43000; downNight.night.l=42000; downNight.futures.foreign_night=-1200;
const downNightOut=v9ProSynthesisAnalysis(downNight);
if(!downNightOut.night.target.includes("夜盤弱勢才獲得進一步價格確認")) throw Error("negative night move missing bearish confirmation conditions");

// Zero is a valid numeric flow/OI value, but not a valid Taiwan index price or option wall.
const zero=JSON.parse(JSON.stringify(fixture));
zero.day.c=0; zero.night.c=0; zero.night.l=0; zero.futures.foreign_night=0; zero.futures.foreign_oi=0;
zero.spot.close=44920; zero.options.putWall=0; zero.options.callWall=48000;
const zeroOut=v9ProSynthesisAnalysis(zero);
if(!zeroOut.night.look.includes("日盤收 缺值")||!zeroOut.night.look.includes("外資夜盤淨交易 0 口")||!zeroOut.night.look.includes("外資期貨 OI 0 口")) throw Error("zero price/flow/OI semantics are inconsistent");
if(!zeroOut.night.target.includes("暫不提供價位觸發條件")) throw Error("zero night low treated as a valid price level");
if(!zeroOut.scenarios.look.includes("Put Wall 缺值")||zeroOut.scenarios.look.includes("現價位於 Put Wall 與 Call Wall 之間")) throw Error("zero Put Wall incorrectly treated as valid in narrative");
if(zeroOut.trade.target.includes("區間內不追價")) throw Error("zero Put Wall incorrectly triggers range trade plan");

// A malformed/non-square correlation matrix must not be described or drawn as a valid NxN heatmap.
const malformed=JSON.parse(JSON.stringify(fixture));
malformed.analysis.correlation={labels:["A","B","C"],matrix:[[1,0],[0,1]],desc:"invalid dimensions"};
const malformedOut=v9ProSynthesisAnalysis(malformed);
if(!malformedOut.correlation.look.includes("缺值或維度不一致")||malformedOut.correlation.look.includes("矩陣 3×3")) throw Error("malformed correlation matrix reported as valid");
if(v9ProCorrelationMatrixReady(["A","B"],[[1,1.2],[1,1]])) throw Error("out-of-range correlation coefficient accepted");
const reverse=JSON.parse(JSON.stringify(fixture));
reverse.spot.close=43000; reverse.options.putWall=44000; reverse.options.flip=42000; reverse.options.gammaWall=43500;
const reverseOut=v9ProSynthesisAnalysis(reverse);
if(reverseOut.scenarios.compass.includes("偏多價格條件：成立")||!reverseOut.scenarios.compass.includes("偏空價格條件：成立")) throw Error("reverse price state has conflicting bull/bear conditions");
if(!reverseOut.scenarios.target.includes("偏空價位條件具備")) throw Error("reverse price state narrative prioritizes wrong scenario");
console.log("synthesis narrative actual + missing + zero + malformed + reverse fixtures PASS");
"""
        result = subprocess.run([node, "-e", script], capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("synthesis narrative actual + missing + zero + malformed + reverse fixtures PASS", result.stdout)

    def test_futures_analysis_narratives_are_derived_from_live_data(self):
        helper_start = self.html.index("function v9ProFuturesAnalysis(")
        helper_end = self.html.index("function v2(", helper_start)
        helper_source = self.html[helper_start:helper_end]
        for card in ("day", "night", "basis", "oi", "flow"):
            self.assertIn(f"analysis:futuresNarrative.{card}", self.html)

        fixture = {
            "day": {"o": 45000, "h": 45332, "l": 44700, "c": 45256, "diff": -44, "pct": -0.10, "vol": 52221, "basis": 335.86, "prem": 0.75},
            "night": {"o": 45227, "h": 45487, "l": 44271, "c": 44310, "diff": -917, "pct": -2.03, "vol": 38487, "change": -946},
            "futures": {"foreign_oi": -89379, "trust_oi": 89139, "dealer_oi": 1307, "top10": 14239, "foreign_day": 2801, "foreign_night": -1349}
        }
        script = "const fixture=" + __import__("json").dumps(fixture, ensure_ascii=False) + ";\\n" + helper_source + """
const out=v9ProFuturesAnalysis(fixture);
if(!out.day.compass.includes("日內收高於開盤")||!out.day.compass.includes("相對前結算仍下跌 -44 點")) throw Error("day session failed to distinguish open-close from previous settlement");
if(!out.night.compass.includes("夜盤收盤低於日盤收盤")||!out.night.compass.includes("收盤位於夜盤區間下緣")) throw Error("night session structure not identified");
if(!out.basis.compass.includes("正價差")||!out.basis.compass.includes("不能抵銷夜盤跌勢")) throw Error("positive basis incorrectly overrides night decline");
if(!out.oi.look.includes("三大法人合計 +1,067 口")||!out.oi.compass.includes("法人部位分歧")) throw Error("institutional OI split/total not explained");
if(!out.flow.compass.includes("日夜流量方向反轉")||!out.flow.compass.includes("外資淨 OI 存量偏空")) throw Error("day/night flow divergence not explained separately from OI");

// Missing values must stay unavailable and never be converted to zero.
const missing=v9ProFuturesAnalysis({day:{},night:{},futures:{}});
if(!missing.day.compass.includes("資料不足")||!missing.oi.compass.includes("資料不足")||!missing.flow.compass.includes("資料不足")) throw Error("missing futures fields produce directional claims");
if(missing.oi.look.includes("0 口")||missing.flow.look.includes("0 口")) throw Error("missing futures fields were coerced to zero");

// Zero is a valid OI/flow value, distinct from missing data.
const zero=v9ProFuturesAnalysis({day:fixture.day,night:fixture.night,futures:{foreign_oi:0,trust_oi:0,dealer_oi:0,top10:0,foreign_day:0,foreign_night:0}});
if(!zero.oi.look.includes("外資淨 OI 0 口")||!zero.flow.compass.includes("均為零")) throw Error("zero OI/flow was treated as missing");
console.log("futures narratives actual + missing + zero fixtures PASS");
"""
        node = shutil.which("node")
        self.assertIsNotNone(node, "Node.js is required for futures narrative runtime tests")
        result = subprocess.run([node, "-e", script], capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("futures narratives actual + missing + zero fixtures PASS", result.stdout)

    def test_trade_plan_keeps_max_pain_separate_from_support(self):
        self.assertIn('["磁吸參考",`${g(l.maxPain)}`]', self.html)
        self.assertNotIn('["支撐",`${g(l.putWall)} / ${g(l.maxPain)}`]', self.html)

if __name__ == "__main__":
    unittest.main()
