import unittest
from unittest.mock import patch

from src.sources import spot_raw


class TPExHistoricalTablesTests(unittest.TestCase):
    def test_highlight_parses_real_tables_schema_by_field_names(self):
        payload = {
            "tables": [{
                "fields": [
                    "上櫃家數", "總資本額(佰萬元)", "總市值(佰萬元)",
                    "本日總成交值(佰萬元)", "本日總成交股數(張數)",
                    "收市指數", "指數漲跌", "上漲家數", "漲停家數",
                    "下跌家數", "跌停家數", "平盤家數", "未成交(含暫停交易)家數",
                ],
                "data": [[
                    "898", "846,606", "8,939,164", "170,543", "1,016,875",
                    "319.12", "-23.29", "97", "24", "746", "85", "35", "20",
                ]],
            }],
            "date": "20261116",
            "flagField": [],
            "stat": "ok",
        }
        with patch.object(spot_raw, "_get_json", return_value=payload):
            result = spot_raw.tpex_highlight("1151116")
        self.assertTrue(result["date_ok"])
        self.assertEqual(result["row"]["PriceRiseCompanyNumbers"], "97")
        self.assertEqual(result["row"]["PriceDeclineCompanyNumbers"], "746")
        self.assertEqual(result["row"]["PriceFlatCompanyNumbers"], "35")
        self.assertEqual(result["row"]["LimitUpCompanyNumbers"], "24")
        self.assertEqual(result["row"]["LimitDownCompanyNumbers"], "85")
        self.assertEqual(result["row"]["DailyTradingValue"], "170,543")

    def test_highlight_rejects_wrong_response_date(self):
        payload = {"tables": [{"fields": ["上漲家數"], "data": [["97"]]}],
                   "date": "20261117", "stat": "ok"}
        with patch.object(spot_raw, "_get_json", return_value=payload):
            result = spot_raw.tpex_highlight("1151116")
        self.assertFalse(result["date_ok"])
        self.assertIsNone(result["row"])

    def test_st41_finds_requested_date_inside_monthly_tables(self):
        payload = {
            "tables": [{
                "fields": ["日期", "成交張數", "金額（仟元）", "筆數", "櫃買指數", "漲/跌"],
                "data": [
                    ["115/11/02", "687,422", "154,820,241", "685,524", 369.24, -1.02],
                    ["115/11/16", "700,000", "160,000,000", "700,000", 319.12, -23.29],
                ],
            }],
            "date": "20261101",
            "stat": "ok",
        }
        with patch.object(spot_raw, "_get_json", return_value=payload):
            result = spot_raw.tpex_turnover_st41("1151116")
        self.assertTrue(result["date_ok"])
        self.assertEqual(result["value"], 160000000.0)

    def test_st41_does_not_substitute_first_day_for_missing_target(self):
        payload = {
            "tables": [{
                "fields": ["日期", "成交張數", "金額（仟元）", "筆數", "櫃買指數", "漲/跌"],
                "data": [["115/11/02", "687,422", "154,820,241", "685,524", 369.24, -1.02]],
            }],
            "date": "20261101",
            "stat": "ok",
        }
        with patch.object(spot_raw, "_get_json", return_value=payload):
            result = spot_raw.tpex_turnover_st41("1151116")
        self.assertFalse(result["date_ok"])
        self.assertIsNone(result["value"])


if __name__ == "__main__":
    unittest.main()
