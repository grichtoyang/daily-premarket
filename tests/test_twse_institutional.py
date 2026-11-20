import unittest
from types import SimpleNamespace
from unittest.mock import patch

from src.sources import twse


class _Response:
    def __init__(self, payload):
        self._payload = payload

    def json(self):
        return self._payload


def _bfi_payload(date="2026-11-19", total="-999,999,999,999"):
    return {
        "stat": "OK",
        "date": date,
        "data": [
            ["外資及陸資", "", "", "-24,312,000,000"],
            ["外資自營商", "", "", "0"],
            ["投信", "", "", "4,390,000,000"],
            ["自營商(自行買賣)", "", "", "-15,000,000,000"],
            ["自營商(避險)", "", "", "-8,303,000,000"],
            ["合計", "", "", total],
        ],
    }


class TWSEInstitutionalConsistencyTests(unittest.TestCase):
    @patch("src.sources.twse._proxy_institutional", return_value=None)
    @patch("src.sources.twse._fetch")
    def test_fallback_accepts_exact_20261105_reproduction_payload(self, fetch, _proxy):
        payload = {
            "stat": "OK",
            "date": "2026/11/05",
            "data": [
                ["外資及陸資", "", "", "100,000,000"],
                ["外資自營商", "", "", "0"],
                ["投信", "", "", "200,000,000"],
                ["自營商(自行買賣)", "", "", "300,000,000"],
                ["自營商(避險)", "", "", "-100,000,000"],
            ],
        }
        fetch.return_value = _Response(payload)

        result = twse.get_institutional("20261105")

        self.assertEqual(result["date"], "20261105")
        self.assertAlmostEqual(result["foreign"], 1.0)
        self.assertAlmostEqual(result["trust"], 2.0)
        self.assertAlmostEqual(result["dealer"], 2.0)
        self.assertAlmostEqual(result["total"], 5.0)

    def test_exact_interactive_simple_namespace_reproduction(self):
        payload = {
            "stat": "OK",
            "date": "2026/11/05",
            "data": [
                ["外資及陸資", "", "", "100,000,000"],
                ["外資自營商", "", "", "0"],
                ["投信", "", "", "200,000,000"],
                ["自營商(自行買賣)", "", "", "300,000,000"],
                ["自營商(避險)", "", "", "-100,000,000"],
            ],
        }
        response = SimpleNamespace(json=lambda: payload)
        with patch.object(twse, "_proxy_institutional", return_value=None), \\
             patch.object(twse, "_fetch", return_value=response):
            result = twse.get_institutional("20261105")

        self.assertEqual(result["date"], "20261105")
        self.assertAlmostEqual(result["foreign"], 1.0)
        self.assertAlmostEqual(result["trust"], 2.0)
        self.assertAlmostEqual(result["dealer"], 2.0)
        self.assertAlmostEqual(result["total"], 5.0)

    @patch("src.sources.twse._proxy_institutional", return_value=None)
    @patch("src.sources.twse._fetch")
    def test_fallback_uses_day_date_and_worker_equivalent_aggregation(self, fetch, _proxy):
        fetch.return_value = _Response(_bfi_payload())
        result = twse.get_institutional("20261119")

        self.assertEqual(fetch.call_args.args[0], twse.BFI82U_URL)
        self.assertEqual(fetch.call_args.kwargs["params"], {
            "dayDate": "20261119", "type": "day", "response": "json"
        })
        self.assertEqual(result["date"], "20261119")
        self.assertAlmostEqual(result["foreign"], -243.12)
        self.assertAlmostEqual(result["trust"], 43.90)
        self.assertAlmostEqual(result["dealer"], -233.03)
        self.assertAlmostEqual(result["total"], -432.25)
        self.assertNotEqual(result["total"], -9999.99999999)

    @patch("src.sources.twse._proxy_institutional", return_value=None)
    @patch("src.sources.twse._fetch")
    def test_total_is_unavailable_when_any_institution_category_is_missing(self, fetch, _proxy):
        payload = _bfi_payload()
        payload["data"] = [row for row in payload["data"] if "投信" not in row[0]]
        fetch.return_value = _Response(payload)

        result = twse.get_institutional("20261119")

        self.assertEqual(result, {})

    @patch("src.sources.twse._proxy_institutional", return_value=None)
    @patch("src.sources.twse._fetch")
    def test_fallback_rejects_upstream_date_mismatch(self, fetch, _proxy):
        fetch.return_value = _Response(_bfi_payload(date="2026-11-18"))

        result = twse.get_institutional("20261119")

        self.assertEqual(result, {})

    @patch("src.sources.twse._proxy_institutional")
    def test_proxy_path_is_used_when_complete_and_date_matched(self, proxy):
        proxy.return_value = {
            "date": "20261119", "foreign": -243.12, "trust": 43.90,
            "dealer": -233.03, "total": -432.25, "via": "proxy"
        }
        result = twse.get_institutional("20261119")
        self.assertEqual(result["via"], "proxy")
        self.assertAlmostEqual(result["total"], -432.25)

    @patch("requests.get")
    def test_proxy_rejects_incomplete_institutional_payload(self, get):
        response = get.return_value
        response.status_code = 200
        response.json.return_value = {
            "ok": True,
            "actual_date": "2026-11-19",
            "date_mismatch": False,
            "data": {
                "foreign": -243.12,
                "investment_trust": None,
                "dealer": -233.03,
                "total": None,
            },
        }
        self.assertIsNone(twse._proxy_institutional("20261119"))

    @patch("requests.get")
    def test_proxy_accepts_complete_institutional_payload(self, get):
        response = get.return_value
        response.status_code = 200
        response.json.return_value = {
            "ok": True,
            "actual_date": "2026-11-19",
            "date_mismatch": False,
            "data": {
                "foreign": -243.12,
                "investment_trust": 43.90,
                "dealer": -233.03,
                "total": -432.25,
            },
        }
        result = twse._proxy_institutional("20261119")
        self.assertEqual(result["date"], "20261119")
        self.assertAlmostEqual(result["total"], -432.25)
        self.assertEqual(result["via"], "proxy")


if __name__ == "__main__":
    unittest.main()
