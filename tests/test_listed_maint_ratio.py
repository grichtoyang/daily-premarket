import unittest
from unittest.mock import patch
import requests

from src.sources.listed_maint_ratio import calculate, get


class ListedMaintenanceRatioTests(unittest.TestCase):
    def fixtures(self):
        margin = {
            "date": "20261030",
            "tables": [
                {"fields": ["項目", "買進", "賣出", "現金(券)償還", "前日餘額", "今日餘額"],
                 "data": [["融資金額(仟元)", "0", "0", "0", "0", "1000"]]},
                {"fields": ["代號", "名稱", "買進", "賣出", "現金償還", "前日餘額", "今日餘額",
                            "次一營業日限額", "買進", "賣出", "現券償還", "前日餘額",
                            "今日餘額", "次一營業日限額", "資券互抵", "註記"],
                 "data": [["2330", "台積電", "0", "0", "0", "10", "10", "100",
                           "0", "0", "0", "0", "999", "100", "0", ""]]},
            ],
        }
        prices = {
            "date": "20261030",
            "tables": [{"fields": ["證券代號", "證券名稱", "收盤價"],
                        "data": [["2330", "台積電", "100"]]}],
        }
        return margin, prices

    def test_calculates_listed_only_ratio(self):
        result = calculate("2026-10-30", *self.fixtures())
        self.assertTrue(result["ok"])
        self.assertEqual(result["ratio"], 100.0)
        self.assertEqual(result["market"], "listed")
        self.assertEqual(result["coverage"], 1.0)
        self.assertEqual(result["financed_security_count"], 1)

    def test_rejects_margin_date_mismatch(self):
        margin, prices = self.fixtures()
        margin["date"] = "20261029"
        with self.assertRaisesRegex(ValueError, "date mismatch"):
            calculate("2026-10-30", margin, prices)

    def test_rejects_price_date_mismatch(self):
        margin, prices = self.fixtures()
        prices["date"] = "20261029"
        with self.assertRaisesRegex(ValueError, "date mismatch"):
            calculate("2026-10-30", margin, prices)

    def test_rejects_missing_same_day_close(self):
        margin, prices = self.fixtures()
        prices["tables"][0]["data"] = []
        with self.assertRaisesRegex(ValueError, "missing T0 close"):
            calculate("2026-10-30", margin, prices)


    def test_uses_explicit_historical_close_for_no_trade_security(self):
        margin, prices = self.fixtures()
        prices["tables"][0]["data"] = []
        result = calculate(
            "2026-10-30", margin, prices,
            historical_prices={"2330": ("20261029", 95.0)},
        )
        self.assertTrue(result["ok"])
        self.assertEqual(result["ratio"], 95.0)
        self.assertEqual(result["stale_price_security_count"], 1)
        self.assertEqual(result["price_date_min"], "20261029")

    def test_rejects_zero_financing_amount(self):
        margin, prices = self.fixtures()
        margin["tables"][0]["data"][0][5] = "0"
        with self.assertRaisesRegex(ValueError, "non-positive"):
            calculate("2026-10-30", margin, prices)

    @patch("src.sources.listed_maint_ratio.requests.get")
    def test_network_failure_returns_unavailable_with_bounded_timeout(self, get_request):
        get_request.side_effect = requests.Timeout("simulated timeout")
        result = get("2026-10-30", timeout=0.2)
        self.assertFalse(result["ok"])
        self.assertIsNone(result["ratio"])
        self.assertIn("timeout", result["reason"].lower())
        self.assertLessEqual(get_request.call_args.kwargs["timeout"], 0.2)


if __name__ == "__main__":
    unittest.main()
