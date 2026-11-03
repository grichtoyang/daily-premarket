import unittest
from unittest.mock import patch

from src.sources import spot_raw


class TWT93USourceTests(unittest.TestCase):
    @patch("src.sources.spot_raw._get_json")
    def test_roc_date_is_converted_to_ad_and_named_fields_are_used(self, get_json):
        get_json.return_value = {
            "stat": "OK", "date": "115/10/30",
            "fields": [
                "代號", "名稱", "前日餘額", "賣出", "買進", "現券",
                "今日餘額", "次一營業日限額", "前日餘額", "當日賣出",
                "當日還券", "當日調整", "當日餘額",
                "次一營業日可限額", "備註",
            ],
            "data": [["2330", "台積電", "1", "2", "3", "0", "4", "5",
                      "100", "20", "10", "0", "110", "200", ""]],
        }
        result = spot_raw.twse_twt93u_sbl("1151030")
        get_json.assert_called_once_with(
            "https://www.twse.com.tw/rwd/zh/marginTrading/TWT93U?response=json&date=20261030"
        )
        self.assertEqual(result["prev_bal"], 100)
        self.assertEqual(result["sale_bal"], 110)
        self.assertEqual(result["sale_chg"], 10)
        self.assertTrue(result["date_ok"])

    @patch("src.sources.spot_raw._get_json")
    def test_field_order_does_not_change_mapping(self, get_json):
        get_json.return_value = {
            "stat": "OK", "date": "2026/10/30",
            "fields": ["名稱", "借券賣出當日餘額", "代號", "借券賣出前日餘額"],
            "data": [["台積電", "110", "2330", "100"]],
        }
        result = spot_raw.twse_twt93u_sbl("2026-10-30")
        self.assertEqual(result["sale_bal"], 110)
        self.assertEqual(result["sale_chg"], 10)

    @patch("src.sources.spot_raw._get_json")
    def test_missing_semantic_fields_fails_closed(self, get_json):
        get_json.return_value = {
            "stat": "OK", "date": "115/10/30", "fields": ["代號", "名稱", "融券前日餘額"],
            "data": [["2330", "台積電", "10"]],
        }
        result = spot_raw.twse_twt93u_sbl("1151030")
        self.assertIsNone(result["sale_bal"])
        self.assertFalse(result["date_ok"])

    @patch("src.sources.spot_raw._get_json")
    def test_non_ok_response_fails_closed(self, get_json):
        get_json.return_value = {"stat": "查詢日期錯誤", "fields": [], "data": []}
        result = spot_raw.twse_twt93u_sbl("1151030")
        self.assertIsNone(result["sale_bal"])
        self.assertFalse(result["date_ok"])


class TWT72USourceTests(unittest.TestCase):
    @patch("src.sources.spot_raw._get_json")
    def test_twt72u_uses_dated_slbnlb_and_sums_stock_rows(self, get_json):
        get_json.return_value = {
            "stat": "OK", "date": "115/10/30",
            "fields": ["證券代號", "證券名稱", "前日借券餘額(1)股",
                       "本日異動股借券(2)", "本日異動股還券(3)",
                       "本日借券餘額股(4)=(1)+(2)-(3)"],
            "data": [
                ["2330", "台積電", "1000", "200", "100", "1100"],
                ["2317", "鴻海", "2000", "300", "100", "2200"],
                ["合計", "", "3000", "500", "200", "3300"],
            ],
        }
        result = spot_raw.twse_twt72u_sbl("1151030")
        get_json.assert_called_once_with(
            "https://www.twse.com.tw/rwd/zh/lending/TWT72U?response=json&date=20261030&selectType=SLBNLB"
        )
        self.assertEqual(result["prev_bal"], 3000)
        self.assertEqual(result["bal"], 3300)
        self.assertEqual(result["chg"], 300)
        self.assertTrue(result["date_ok"])

    @patch("src.sources.spot_raw._get_json")
    def test_twt72u_date_mismatch_fails_closed(self, get_json):
        get_json.return_value = {
            "stat": "OK", "date": "115/10/29",
            "fields": ["證券代號", "前日借券餘額(1)股", "本日借券餘額股(4)=(1)+(2)-(3)"],
            "data": [["2330", "100", "110"]],
        }
        result = spot_raw.twse_twt72u_sbl("1151030")
        self.assertIsNone(result["bal"])
        self.assertFalse(result["date_ok"])


class TPEXSBLS47SourceTests(unittest.TestCase):
    @patch("src.sources.spot_raw._get_json")
    def test_tpex_s47_uses_named_borrowed_short_fields_and_exact_date(self, get_json):
        get_json.return_value = {
            "date": "115/10/30",
            "tables": [{
                "fields": ["股票代號", "股票名稱", "前日餘額", "賣出",
                           "買進", "現券", "當日餘額", "限額",
                           "前日餘額", "當日賣出", "當日還券",
                           "當日調整數額", "當日餘額",
                           "次一營業日可借券賣出限額", "備註"],
                "data": [
                    ["6488", "環球晶", "10", "1", "0", "0", "11", "1000",
                     "1000", "200", "100", "0", "1100", "5000", ""],
                    ["合計", "", "10", "1", "0", "0", "11", "1000",
                     "1000", "200", "100", "0", "1100", "5000", ""],
                ],
            }],
        }
        result = spot_raw.tpex_sbl("1151030")
        get_json.assert_called_once_with(
            "https://www.tpex.org.tw/www/zh-tw/margin/sbl?response=json&date=2026/10/30"
        )
        self.assertEqual(result["sale_bal"], 1100)
        self.assertEqual(result["sale_chg"], 100)
        self.assertTrue(result["date_ok"])

    @patch("src.sources.spot_raw._get_json")
    def test_tpex_s47_missing_date_fails_closed(self, get_json):
        get_json.return_value = {
            "tables": [{"fields": ["證券代號", "借券賣出前日餘額", "借券賣出當日餘額"],
                        "data": [["6488", "100", "110"]]}]
        }
        result = spot_raw.tpex_sbl("1151030")
        self.assertIsNone(result["sale_bal"])
        self.assertFalse(result["date_ok"])


if __name__ == "__main__":
    unittest.main()
