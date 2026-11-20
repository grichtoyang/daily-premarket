import unittest
from unittest.mock import patch

from src.sources import treasury


class _Response:
    status_code = 200

    def __init__(self, text):
        self.text = text

    def raise_for_status(self):
        return None


class TreasuryXmlFallbackTests(unittest.TestCase):
    def test_fetches_xml_once_for_both_missing_tenors(self):
        xml = """<ROOT>
        <G_NEW_DATE><BID_CURVE_DATE>11/19/2026</BID_CURVE_DATE><BC_2YEAR>3.50</BC_2YEAR><BC_20YEAR>4.60</BC_20YEAR></G_NEW_DATE>
        <G_NEW_DATE><BID_CURVE_DATE>11/20/2026</BID_CURVE_DATE><BC_2YEAR>3.55</BC_2YEAR><BC_20YEAR>4.65</BC_20YEAR></G_NEW_DATE>
        </ROOT>"""

        with patch.object(treasury, "_treasury", return_value=None), \
             patch("requests.get", return_value=_Response(xml)) as get, \
             patch.object(treasury, "quote", return_value={
                 "price": 4.2, "change": 0.1, "date": "2026-11-20",
                 "retrieved_at": "2026-11-20T08:00:00+00:00", "ok": True,
             }):
            result = treasury.get_yields()

        self.assertEqual(get.call_count, 1)
        self.assertEqual(result["2Y"]["yield"], 3.55)
        self.assertAlmostEqual(result["2Y"]["chg"], 0.05)
        self.assertEqual(result["2Y"]["date"], "11/20/2026")
        self.assertEqual(result["20Y"]["yield"], 4.65)
        self.assertAlmostEqual(result["20Y"]["chg"], 0.05)
        self.assertEqual(result["20Y"]["date"], "11/20/2026")
        self.assertTrue(result["2Y"]["ok"])
        self.assertTrue(result["20Y"]["ok"])
        self.assertEqual(result["10Y"]["yield"], 4.2)
        self.assertEqual(result["30Y"]["yield"], 4.2)

    def test_only_fetches_xml_when_an_xml_tenor_is_missing(self):
        with patch.object(treasury, "_treasury", return_value={
            "2Y": {"yield": 3.5, "chg": 0.0, "date": "2026-11-20", "ok": True},
            "10Y": {"yield": 4.2, "chg": 0.1, "date": "2026-11-20", "ok": True},
            "20Y": {"yield": 4.6, "chg": 0.0, "date": "2026-11-20", "ok": True},
            "30Y": {"yield": 4.8, "chg": 0.0, "date": "2026-11-20", "ok": True},
        }), patch("requests.get") as get:
            result = treasury.get_yields()

        get.assert_not_called()
        self.assertEqual(result["2Y"]["yield"], 3.5)
        self.assertEqual(result["20Y"]["yield"], 4.6)


if __name__ == "__main__":
    unittest.main()
