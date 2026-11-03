import unittest
from collections import Counter
import re
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
            stock_markets = {"集中市場", "櫃檯買賣中心"}
            bad_rows = [
                (row[0], row[market_index], row[5])
                for row in payload.get("data", [])
                if len(row) > market_index and str(row[market_index]).strip() in stock_markets
                and not re.fullmatch(r"[0-9A-Z]{4,6}", str(row[0] or "").strip().upper())
            ]
            print("TWT72U_BAD_STOCK_CODES", bad_rows[:20], "count=", len(bad_rows))
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
        fields = payload.get("fields") or []
        for label in ("當日賣出", "當日還券", "當日調整"):
            if label in fields:
                idx = fields.index(label)
                print("TWT93U_FLOW_FIELD", label, "blank_rows=", sum(1 for row in payload.get("data", []) if len(row) > idx and not str(row[idx]).strip()), "sample=", [row[idx] for row in payload.get("data", [])[:3] if len(row) > idx])
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
        fields = table.get("fields") or []
        for label in ("當日賣出", "當日還券", "當日調整數額"):
            if label in fields:
                idx = fields.index(label)
                print("TPEX_S47_FLOW_FIELD", label, "blank_rows=", sum(1 for row in table.get("data", []) if len(row) > idx and not str(row[idx]).strip()), "sample=", [row[idx] for row in table.get("data", [])[:3] if len(row) > idx])
        with patch("src.sources.spot_raw._get_json", return_value=payload):
            parsed = spot_raw.tpex_sbl(T0)
        self.assertTrue(parsed["date_ok"], parsed)
        self.assertGreater(parsed["sale_bal"], 0, parsed)


if __name__ == "__main__":
    unittest.main(verbosity=2)
