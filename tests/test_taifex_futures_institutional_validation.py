import unittest
from unittest.mock import Mock, patch
from src.sources import taifex


def payload(day="2026-11-27"):
    return {
        "ok": True, "date": day,
        "data": [
            {"institution": institution, "long_volume": 1, "long_amount": 2,
             "short_volume": 3, "short_amount": 4, "net_volume": 5, "net_amount": 6}
            for institution in ("foreign", "investment_trust", "dealer")
        ],
    }


class FuturesInstitutionalValidationTests(unittest.TestCase):
    def response(self, data):
        response = Mock()
        response.status_code = 200
        response.json.return_value = data
        return response

    @patch("time.sleep")
    @patch("src.sources.taifex.requests.get")
    def test_accepts_complete_t0_payload(self, get, _sleep):
        get.return_value = self.response(payload())
        result = taifex._get_impl("futures-institutional", "2026-11-27")
        self.assertEqual(result["date"], "2026-11-27")
        get.assert_called_once()

    @patch("time.sleep")
    @patch("src.sources.taifex.requests.get")
    def test_rejects_stale_payload_and_retries_once(self, get, _sleep):
        get.return_value = self.response(payload("2026-11-26"))
        self.assertIsNone(taifex._get_impl("futures-institutional", "2026-11-27"))
        self.assertEqual(get.call_count, 2)
        self.assertIn("date_mismatch", taifex._LAST_FETCH_ERRORS["futures-institutional"]["detail"])

    @patch("time.sleep")
    @patch("src.sources.taifex.requests.get")
    def test_rejects_missing_date(self, get, _sleep):
        data = payload()
        data.pop("date")
        get.return_value = self.response(data)
        self.assertIsNone(taifex._get_impl("futures-institutional", "2026-11-27"))

    @patch("time.sleep")
    @patch("src.sources.taifex.requests.get")
    def test_rejects_empty_data(self, get, _sleep):
        data = payload()
        data["data"] = []
        get.return_value = self.response(data)
        self.assertIsNone(taifex._get_impl("futures-institutional", "2026-11-27"))

    @patch("time.sleep")
    @patch("src.sources.taifex.requests.get")
    def test_rejects_duplicate_category(self, get, _sleep):
        data = payload()
        data["data"][2] = dict(data["data"][1])
        get.return_value = self.response(data)
        self.assertIsNone(taifex._get_impl("futures-institutional", "2026-11-27"))

    @patch("time.sleep")
    @patch("src.sources.taifex.requests.get")
    def test_rejects_missing_numeric_value(self, get, _sleep):
        data = payload()
        data["data"][0]["net_volume"] = None
        get.return_value = self.response(data)
        self.assertIsNone(taifex._get_impl("futures-institutional", "2026-11-27"))

    def test_zero_is_valid_numeric_data(self):
        data = payload()
        data["data"][0]["net_volume"] = 0
        self.assertEqual(
            taifex._valid_futures_institutional_payload(data, "2026-11-27"),
            (True, None),
        )

    @patch("src.sources.taifex._previous_trading_day_iso", return_value="2026-11-26")
    @patch("src.sources.taifex.snapshot_bundle", return_value=None)
    @patch("src.sources.taifex._night_ohlc", return_value=None)
    @patch("src.sources.taifex._prev_dates", return_value=[])
    @patch("src.sources.taifex._night_query_date", return_value=None)
    @patch("src.sources.taifex._memoized_build_fetch")
    def test_build_does_not_use_stale_institutional_rows(self, cache_factory, *_mocks):
        def fake_fetch(_get):
            return lambda ep, day, timeout=40: (
                payload("2026-11-26") if ep == "futures-institutional" else None
            )
        cache_factory.side_effect = fake_fetch
        result = taifex.build("2026-11-27", session="日盤")
        self.assertIsNone(result["fut_trade"][("day", "foreign")]["net"])
        self.assertTrue(any("期貨日盤三大法人資料拒收" in note for note in result["notes"]))


if __name__ == "__main__":
    unittest.main()
