from pathlib import Path
import json
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class DashboardUnitContractTests(unittest.TestCase):
    def test_data_report_template_matches_builder_units(self):
        template = (ROOT / "docs" / "DATA_REPORT_TEMPLATE.md").read_text(encoding="utf-8")
        builder = (ROOT / "scripts" / "v9_pro_builder.py").read_text(encoding="utf-8")
        self.assertIn("融資餘額/增減 (億元)", template)
        self.assertIn("融券餘額 (張)", template)
        self.assertIn("借券餘額/借券賣出餘額/賣出增減 (張", template)
        self.assertIn(r"融資餘額 \| ([0-9,.]+) \| 億元", builder)
        self.assertIn(r"融券餘額 \| ([0-9,]+) \| 張", builder)
        self.assertIn(r"借券餘額 \| ([0-9,]+) \| 張", builder)
        self.assertIn('fut_day_o=must_get(r"### 1．台指期近月日盤行情.*?開盤價', builder)
        self.assertIn('basis=optional_get(r"台指期與加權指數價差', builder)
        fetch_data = (ROOT / "src" / "fetch_data.py").read_text(encoding="utf-8")
        self.assertIn('"unit": "NTD per 1% underlying move"', fetch_data)
        self.assertIn("NT$／標的變動 1%", fetch_data)
        worker = (ROOT / "workers" / "taifex-proxy_V1.4.js").read_text(encoding="utf-8")
        self.assertIn("gamma *\n      oi *\n      50 *\n      underlyingPrice *\n      underlyingPrice *\n      0.01", worker)
        self.assertIn('call_vol=must_get(r"Call 總成交量', builder)
        self.assertIn('pcr=optional_get(r"Put／Call Ratio', builder)

    def test_futures_trade_table_has_per_row_units(self):
        fetch_data = (ROOT / "src" / "fetch_data.py").read_text(encoding="utf-8")
        self.assertIn('("法人日盤交易金額淨額", _f1s(', fetch_data)
        self.assertIn('"億元", SRC_FX)', fetch_data)
        self.assertIn('("項目", "數值", "單位", "資料來源")', fetch_data)
        self.assertIn('("外資日盤多單交易量", _fi(', fetch_data)
        self.assertIn('"口", SRC_FX)', fetch_data)

    def test_option_ratio_changes_use_percentage_points(self):
        fetch_data = (ROOT / "src" / "fetch_data.py").read_text(encoding="utf-8")
        standard = (ROOT / "docs" / "DASHBOARD_UNIT_STANDARD.md").read_text(encoding="utf-8")
        self.assertIn('("Call／Put 成交量比例", _f2(_ot[\'vol_ratio\']), "倍"', fetch_data)
        self.assertIn('"百分點（pp）", _pch_src)', fetch_data)
        self.assertIn('("項目", "數值", "單位", "資料來源")', fetch_data)
        self.assertIn("日變化為百分點（pp）", standard)

    def test_treasury_yield_curve_includes_20_year(self):
        treasury = (ROOT / "src" / "sources" / "treasury.py").read_text(encoding="utf-8")
        fetch_data = (ROOT / "src" / "fetch_data.py").read_text(encoding="utf-8")
        self.assertIn('("20Y", ("20 Yr", "20yr", "bc_20year"))', treasury)
        self.assertIn('_xml_yield("BC_20YEAR")', treasury)
        self.assertIn('y["20Y"]["yield"]', fetch_data)
        self.assertIn('("美國 20 年期殖利率", "20 Yr"', fetch_data)

    def test_unit_standard_and_skill_are_present(self):
        standard = (ROOT / "docs" / "DASHBOARD_UNIT_STANDARD.md").read_text(encoding="utf-8")
        skill = (ROOT / "skills" / "daily-premarket-analysis-v9-pro-skill.md").read_text(encoding="utf-8")
        for term in ("來源單位", "Builder 標準單位", "Dashboard 顯示單位", "百分點", "混合單位", "BLOCKED"):
            self.assertIn(term, standard)
        self.assertIn("Dashboard 數字單位與圖表版面驗收", skill)
        self.assertIn("42 個可見 Dashboard 區塊", skill)
        registry = json.loads((ROOT / "docs" / "DASHBOARD_UNIT_REGISTRY.json").read_text(encoding="utf-8"))
        self.assertEqual(registry["metrics"]["options.pcr"]["display_unit"], "倍")
        self.assertEqual(registry["metrics"]["options.gex.net_gross_per_strike"]["display_unit"], "NT$／標的價格變動 1%")
        self.assertEqual(registry["metrics"]["options.gex.net_gross_per_strike"]["status"], "defined_by_worker_formula")
        unit_map = (ROOT / "docs" / "DASHBOARD_UNIT_MAP.md").read_text(encoding="utf-8")
        self.assertIn("42 區塊", unit_map)
        self.assertIn("履約價 GEX 分布", unit_map)
        self.assertIn("spot.otc.up/down/flat/limit_up/limit_down", unit_map)
        self.assertIn("parse_data_report()", unit_map)
        self.assertNotIn("GEX 單位 BLOCKED", unit_map)
        self.assertIn("2026-11-02 完整欄位語義稽核", unit_map)
        self.assertEqual(len(re.findall(r"^\|\s*(?:[1-9]|[1-3][0-9]|4[0-2])\s*\|.*\| PASS \|", unit_map, re.MULTILINE)), 42)
        self.assertIn("GEX 正負不得直接轉成 Bias 多空分數", standard)
        self.assertIn("T0", standard)
        self.assertIn("semantic_note", registry["metrics"]["options.gex.net_gross_per_strike"])
        self.assertIn("history.similarity_outcomes", registry["metrics"])
        self.assertIn("technical.indicators", registry["metrics"])
        self.assertIn("analysis_card_count", (ROOT / "scripts" / "v9_pro_builder.py").read_text(encoding="utf-8"))

    def test_spot_turnover_uses_turnover_chart_not_options_volume_chart(self):
        html = (ROOT / "templates" / "v9-pro-react-template.html").read_text(encoding="utf-8")
        self.assertIn('chart:p(Ol,{items:[{l:"上市",v:o.listed,extra:"億元"},{l:"上櫃",v:o.otc,extra:"億元"},{l:"合計",v:o.total,extra:"億元"}]', html)
        self.assertIn('function yf({callVol:e,putVol:n,height:l=200})', html)

    def test_chart_notes_and_unit_contracts(self):
        html = (ROOT / "templates" / "v9-pro-react-template.html").read_text(encoding="utf-8")
        self.assertIn("chartNote:chartNote", html)
        self.assertIn('volUnit:unitLabel="口"', html)
        self.assertIn('s.fillText(`VOL ${g(o)}${unitLabel}`,S+Ee+10,A+11)', html)
        self.assertNotIn('s.fillText(`VOL ${g(o)}${a}`,S+Ee+10,A+11)', html)
        self.assertIn('volUnit:"億元"', html)
        self.assertIn('changeUnit:o.key==="yields"?"pp":"%"', html)
        self.assertIn('殖利率水準：%；日變化：百分點（pp）。', html)
        self.assertIn('履約價／現價／Call Wall／Put Wall：點；OI：口。', html)
        self.assertIn("GEX：新台幣元（NT$）", html)
        self.assertIn("function Fl({title:e,subtitle:n,chart:r,chartNote:chartNote", html)
        self.assertIn('chartNote:"5 日收盤與所有關鍵水位：點。"', html)
        self.assertIn('chartNote:"單位：億元；法人買賣超，正值買超、負值賣超。"', html)
        self.assertIn('chartNote:"現價與 Call／Put Wall、Gamma Wall、Flip、Max Pain：點；Net GEX：NT$／標的變動 1%。"', html)
        self.assertIn('chartNote:"漲跌幅：%；收盤價：各指數點。"', html)
        self.assertIn("USD/TWD、USD/JPY、USD/KRW 報價為每美元兌本幣；DXY 為指數點。", html)
        self.assertIn("WTI：USD／桶；黃金：USD／金衡盎司；Bitcoin：USD／BTC。", html)
        self.assertIn("TWD／每 USD", html)
        self.assertIn("JPY／每 USD", html)
        self.assertIn("KRW／每 USD", html)

    def test_missing_source_values_remain_unavailable_not_zero(self):
        builder = (ROOT / "scripts" / "v9_pro_builder.py").read_text(encoding="utf-8")
        self.assertIn("flat=int(flat_match.group(1)) if flat_match else None", builder)
        self.assertIn("limit_up=int(up_limit_match.group(1)) if up_limit_match else None", builder)
        self.assertIn("otc_section=text.find(\"#### 2.2 上櫃公司\"); otc_up=otc_down=otc_flat=otc_limit_up=otc_limit_down=None", builder)
        self.assertIn('margin_finance=get_value(r"\\| 融資餘額 \\| ([0-9,.]+) \\| 億元",None)', builder)
        html = (ROOT / "templates" / "v9-pro-react-template.html").read_text(encoding="utf-8")
        self.assertIn('F.up,F.down,F.flat].some(P=>P==null||!Number.isFinite(P))', html)
        self.assertIn('融資增減 unavailable', html)
        self.assertIn('validRatio?B(l,2)+"%":"unavailable"', html)

    def test_42_block_registry_and_chart_notes_are_complete(self):
        unit_map = (ROOT / "docs" / "DASHBOARD_UNIT_MAP.md").read_text(encoding="utf-8")
        block_table = unit_map.split("## 42 區塊資料路徑／來源對照", 1)[0]
        block_numbers = [int(value) for value in re.findall(r"^\|\s*(\d+)\s*\|", block_table, re.MULTILINE)]
        self.assertEqual(block_numbers, list(range(1, 43)))

        html = (ROOT / "templates" / "v9-pro-react-template.html").read_text(encoding="utf-8")
        cards = html.split("p(V,{title:")[1:]
        chart_cards = [card.split("}),p(V,{title:", 1)[0] for card in cards]
        self.assertGreater(len(chart_cards), 0)
        missing_notes = []
        for index, card in enumerate(chart_cards, start=1):
            # News cards use the generic `chart` slot for a scrollable text list;
            # only actual chart components require a nearby unit note.
            chart_match = re.search(r"chart:p\(([^,{]+)", card)
            if chart_match and chart_match.group(1) != '"div"' and "chartNote:" not in card:
                title_match = re.search(r'^"([^"]+)"', card)
                missing_notes.append(title_match.group(1) if title_match else f"chart card {index}")
        self.assertEqual(missing_notes, [], f"Charts missing adjacent unit notes: {missing_notes}")
        self.assertIn('chartNote&&p("div"', html)


    def test_existing_data_report_is_protected_without_daily_report(self):
        # The DATA_REPORT itself is the published T0 snapshot. A missing
        # reports/Daily_REPORT file must not switch an existing T0 to overwrite.
        from src.fetch_data import _should_protect_existing_data_report

        self.assertTrue(_should_protect_existing_data_report(True, False))
        self.assertFalse(_should_protect_existing_data_report(True, True))
        self.assertFalse(_should_protect_existing_data_report(False, False))


if __name__ == "__main__":
    unittest.main()
