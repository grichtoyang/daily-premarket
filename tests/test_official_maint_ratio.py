import unittest

from src.sources.official_maint_ratio import calculate


class OfficialMaintenanceRatioTests(unittest.TestCase):
    def fixtures(self):
        twse_margin = {
            "date": "20261030",
            "tables": [
                {"fields": ["項目", "買進", "賣出", "現金(券)償還", "前日餘額", "今日餘額"],
                 "data": [["融資金額(仟元)", "0", "0", "0", "0", "1000"]]},
                {"fields": ["證券代號", "證券名稱", "買進", "賣出", "現金償還", "前日餘額", "今日餘額"],
                 "data": [["2330", "台積電", "0", "0", "0", "10", "10"]]},
            ],
        }
        tpex_margin = {
            "date": "115/10/30",
            "tables": [
                {"fields": ["代號", "名稱", "前資餘額(張)", "資買", "資賣", "現償", "資餘額"],
                 "data": [["6488", "環球晶", "2", "0", "0", "0", "2"]],
                 "summary": [["", "融資金(仟元)", "2000", "0", "0", "0", "2000"]]},
            ],
        }
        twse_prices = {
            "date": "20261030",
            "tables": [
                {"fields": ["證券代號", "證券名稱", "收盤價"],
                 "data": [["2330", "台積電", "100"]]},
            ],
        }
        tpex_prices = {
            "date": "115/10/30",
            "tables": [
                {"fields": ["代號", "名稱", "收盤"],
                 "data": [["6488", "環球晶", "200"]]},
            ],
        }
        return twse_margin, tpex_margin, twse_prices, tpex_prices

    def test_calculates_same_day_combined_ratio(self):
        args = self.fixtures()
        result = calculate("2026-10-30", "115/10/30", *args)
        # (10*1000*100 + 2*1000*200) / ((1000+2000)*1000) * 100
        self.assertTrue(result["ok"])
        self.assertEqual(result["ratio"], 46.6667)
        self.assertEqual(result["coverage"], 1.0)
        self.assertEqual(result["financed_security_count"], 2)

    def test_rejects_missing_close_for_positive_balance(self):
        args = list(self.fixtures())
        args[3]["tables"][0]["data"] = []
        with self.assertRaisesRegex(ValueError, "no same-day close"):
            calculate("2026-10-30", "115/10/30", *args)

    def test_rejects_wrong_tpex_price_date(self):
        args = list(self.fixtures())
        args[3]["date"] = "115/10/29"
        with self.assertRaisesRegex(ValueError, "date mismatch"):
            calculate("2026-10-30", "115/10/30", *args)

    def test_rejects_zero_financing_denominator(self):
        args = list(self.fixtures())
        args[0]["tables"][0]["data"][0][5] = "0"
        args[1]["tables"][0]["summary"][0][6] = "0"
        with self.assertRaisesRegex(ValueError, "must be positive"):
            calculate("2026-10-30", "115/10/30", *args)


if __name__ == "__main__":
    unittest.main()
