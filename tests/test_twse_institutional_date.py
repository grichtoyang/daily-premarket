import unittest
from unittest.mock import patch

from src.sources import spot, twse


class _Response:
    status_code = 200

    def __init__(self, payload):
        self.payload = payload

    def json(self):
        return self.payload


class InstitutionalDateValidationTests(unittest.TestCase):
    def test_normalizes_gregorian_and_roc_dates(self):
        self.assertEqual(twse._normalize_date8("2026-11-05"), "20261105")
        self.assertEqual(twse._normalize_date8("115/11/05"), "20261105")

    @patch("requests.get")
    def test_proxy_rejects_actual_date_mismatch(self, get):
        get.return_value = _Response({
            "ok": True, "actual_date": "20261104", "date": "20261105",
            "date_mismatch": True, "data": {"foreign": 12},
        })
        self.assertIsNone(twse._proxy_institutional("20261105"))

    @patch("requests.get")
    def test_proxy_rejects_missing_actual_date(self, get):
        get.return_value = _Response({
            "ok": True, "date": "20261105", "data": {"foreign": 12},
        })
        self.assertIsNone(twse._proxy_institutional("20261105"))

    @patch("requests.get")
    def test_proxy_accepts_matching_actual_date(self, get):
        get.return_value = _Response({
            "ok": True, "actual_date": "2026-11-05", "date_mismatch": False,
            "data": {"foreign": 12, "investment_trust": 3, "dealer": 2, "total": 17},
        })
        result = twse._proxy_institutional("20261105")
        self.assertEqual(result["date"], "20261105")
        self.assertEqual(result["foreign"], 12)

    @patch("src.sources.twse._proxy_institutional", return_value=None)
    @patch("src.sources.twse._fetch")
    def test_rwd_rejects_mismatched_date(self, fetch, _proxy):
        fetch.return_value = _Response({
            "stat": "OK", "date": "2026/11/04",
            "data": [["外資及陸資", "", "", "100"]],
        })
        self.assertEqual(twse.get_institutional("20261105"), {})

    @patch("src.sources.twse._proxy_institutional", return_value=None)
    @patch("src.sources.twse._fetch")
    def test_rwd_accepts_matching_date(self, fetch, _proxy):
        fetch.return_value = _Response({
            "stat": "OK", "date": "2026/11/05",
            "data": [["外資及陸資", "", "", "100"]],
        })
        result = twse.get_institutional("20261105")
        self.assertEqual(result["date"], "20261105")
        self.assertEqual(result["foreign"], 1.0)

    def test_spot_contract_rejects_missing_or_wrong_date(self):
        self.assertFalse(spot._institutional_matches_t0({"date": "", "foreign": 1}, "20261105"))
        self.assertFalse(spot._institutional_matches_t0({"date": "20261104", "foreign": 1}, "20261105"))
        self.assertTrue(spot._institutional_matches_t0({"date": "2026/11/05", "foreign": 1}, "20261105"))


if __name__ == "__main__":
    unittest.main()
