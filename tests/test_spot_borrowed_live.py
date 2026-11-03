import unittest
from collections import Counter
from unittest.mock import patch

from src.sources import spot_raw


T0 = "1151030"
DATE8 = "20261030"


class LiveBorrowedSourceProbeTests(unittest.TestCase):
    def test_live_twse_twt72u_history(self):
        url = (
            "https://www.twse.com.tw/rwd/zh/lending/TWT72U"
            f"?response=json&date={DATE8}&selectType=SLBNLB"
        )
        payload = spot_raw._get_json(url)
        self.assertIsInstance(payload, dict, f"TWT72U response type: {type(payload).__name__}")
        print("TWT72U_LIVE_META", payload.get("stat"), payload.get("date"), len(payload.get("data") or []))
        print("TWT72U_LIVE_FIELDS", payload.get("fields"))
        fields = payload.get("fields") or []
        if "市場別" in fields:
            market_index = fields.index("市場別")
            print("TWT72U_MARKET_COUNTS", Counter(str(row[market_index]).strip() for row in payload.get("data", []) if len(row) > market_index))
        with patch("src.sources.spot_raw._get_json", return_value=payload):
            parsed = spot_raw.twse_twt72u_sbl(T0)
        self.assertTrue(parsed["date_ok"], parsed)
        self.assertGreater(parsed["bal"], 0, parsed)

    def test_live_twse_twt93u_history(self):
        url = (
            "https://www.twse.com.tw/rwd/zh/marginTrading/TWT93U"
            f"?response=json&date={DATE8}"
        )
        payload = spot_raw._get_json(url)
        self.assertIsInstance(payload, dict, f"TWT93U response type: {type(payload).__name__}")
        print("TWT93U_LIVE_META", payload.get("stat"), payload.get("date"), len(payload.get("data") or []))
        print("TWT93U_LIVE_FIELDS", payload.get("fields"))
        with patch("src.sources.spot_raw._get_json", return_value=payload):
            parsed = spot_raw.twse_twt93u_sbl(T0)
        self.assertTrue(parsed["date_ok"], parsed)
        self.assertGreater(parsed["sale_bal"], 0, parsed)

    def test_live_tpex_s47_history(self):
        url = (
            "https://www.tpex.org.tw/www/zh-tw/margin/sbl"
            f"?response=json&date=2026/10/30"
        )
        payload = spot_raw._get_json(url)
        self.assertIsInstance(payload, dict, f"TPEx S47 response type: {type(payload).__name__}")
        tables = payload.get("tables") or []
        table = next((x for x in tables if isinstance(x, dict)), {})
        print("TPEX_S47_LIVE_META", payload.get("date"), table.get("date"), len(table.get("data") or []))
        print("TPEX_S47_LIVE_FIELDS", table.get("fields"))
        with patch("src.sources.spot_raw._get_json", return_value=payload):
            parsed = spot_raw.tpex_sbl(T0)
        self.assertTrue(parsed["date_ok"], parsed)
        self.assertGreater(parsed["sale_bal"], 0, parsed)


if __name__ == "__main__":
    unittest.main(verbosity=2)
