import unittest
from unittest.mock import patch

from src.sources import spot_raw


class TWT93USourceTests(unittest.TestCase):
    @patch("src.sources.spot_raw._get_json")
    def test_roc_date_is_converted_to_ad_and_named_fields_are_used(self, get_json):
        get_json.return_value = {
            "stat": "OK",
            "fields": [
                "代號", "名稱", "融券前日餘額", "融券賣出", "融券買進",
                "融券現券", "融券當日餘額", "融券限額",
                "借券賣出前日餘額", "借券賣出當日賣出", "借券賣出當日還券",
                "借券賣出當日調整", "借券賣出當日餘額",
                "次一營業日可借券賣出限額", "備註",
            ],
            "data": [["2330", "台積電", "1", "2", "3", "0", "4", "5",
                      "100", "20", "10", "0", "110", "200", ""]],
        }
        result = spot_raw.twse_twt93u_sbl("1151030")
        get_json.assert_called_once_with(
            "https://www.twse.com.tw/exchangeReport/TWT93U?response=json&date=20261030"
        )
        self.assertEqual(result["prev_bal"], 100)
        self.assertEqual(result["sale_bal"], 110)
        self.assertEqual(result["sale_chg"], 10)
        self.assertTrue(result["date_ok"])

    @patch("src.sources.spot_raw._get_json")
    def test_field_order_does_not_change_mapping(self, get_json):
        get_json.return_value = {
            "stat": "OK",
            "fields": ["名稱", "借券賣出當日餘額", "代號", "借券賣出前日餘額"],
            "data": [["台積電", "110", "2330", "100"]],
        }
        result = spot_raw.twse_twt93u_sbl("2026-10-30")
        self.assertEqual(result["sale_bal"], 110)
        self.assertEqual(result["sale_chg"], 10)

    @patch("src.sources.spot_raw._get_json")
    def test_missing_semantic_fields_fails_closed(self, get_json):
        get_json.return_value = {
            "stat": "OK", "fields": ["代號", "名稱", "融券前日餘額"],
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


if __name__ == "__main__":
    unittest.main()
