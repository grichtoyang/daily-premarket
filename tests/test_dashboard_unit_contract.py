from pathlib import Path
import json
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
        self.assertIn('call_vol=must_get(r"Call 總成交量', builder)
        self.assertIn('pcr=optional_get(r"Put／Call Ratio', builder)

    def test_unit_standard_and_skill_are_present(self):
        standard = (ROOT / "docs" / "DASHBOARD_UNIT_STANDARD.md").read_text(encoding="utf-8")
        skill = (ROOT / "skills" / "daily-premarket-analysis-v9-pro-skill.md").read_text(encoding="utf-8")
        for term in ("來源單位", "Builder 標準單位", "Dashboard 顯示單位", "百分點", "混合單位", "BLOCKED"):
            self.assertIn(term, standard)
        self.assertIn("Dashboard 數字單位與圖表版面驗收", skill)
        self.assertIn("42 個可見 Dashboard 區塊", skill)
        registry = json.loads((ROOT / "docs" / "DASHBOARD_UNIT_REGISTRY.json").read_text(encoding="utf-8"))
        self.assertEqual(registry["metrics"]["options.pcr"]["display_unit"], "倍")
        self.assertTrue(registry["metrics"]["options.gex.net_gross_per_strike"]["status"].startswith("blocked"))
        unit_map = (ROOT / "docs" / "DASHBOARD_UNIT_MAP.md").read_text(encoding="utf-8")
        self.assertIn("42 區塊", unit_map)
        self.assertIn("履約價 GEX 分布", unit_map)

    def test_spot_turnover_uses_turnover_chart_not_options_volume_chart(self):
        html = (ROOT / "templates" / "v9-pro-react-template.html").read_text(encoding="utf-8")
        self.assertIn('chart:p(Ol,{items:[{l:"上市",v:o.listed,extra:"億元"},{l:"上櫃",v:o.otc,extra:"億元"},{l:"合計",v:o.total,extra:"億元"}]', html)
        self.assertIn('function yf({callVol:e,putVol:n,height:l=200})', html)

    def test_chart_notes_and_unit_contracts(self):
        html = (ROOT / "templates" / "v9-pro-react-template.html").read_text(encoding="utf-8")
        self.assertIn("chartNote:chartNote", html)
        self.assertIn('volUnit:a="口"', html)
        self.assertIn('volUnit:"億元"', html)
        self.assertIn('changeUnit:o.key==="yields"?"pp":"%"', html)
        self.assertIn('殖利率水準：%；日變化：百分點（pp）。', html)
        self.assertIn('履約價／現價／Call Wall／Put Wall：點；OI：口。', html)


if __name__ == "__main__":
    unittest.main()
