import unittest

from src.fetch_data import _coverage_status_lines


class DataReportCoverageStatusTests(unittest.TestCase):
    def test_partial_only(self):
        self.assertEqual(_coverage_status_lines(["spot.margin_a"], []), [
            "- 部分取得欄位 (1)：spot.margin_a",
            "- 未取得欄位 (0)：無",
        ])

    def test_unavailable_only(self):
        self.assertEqual(_coverage_status_lines([], ["futures.oi"]), [
            "- 部分取得欄位 (0)：無",
            "- 未取得欄位 (1)：futures.oi",
        ])

    def test_partial_and_unavailable(self):
        self.assertEqual(_coverage_status_lines(["spot.margin_a"], ["futures.oi"]), [
            "- 部分取得欄位 (1)：spot.margin_a",
            "- 未取得欄位 (1)：futures.oi",
        ])

    def test_neither(self):
        self.assertEqual(_coverage_status_lines([], []), [
            "- 部分取得欄位 (0)：無",
            "- 未取得欄位 (0)：無",
        ])


if __name__ == "__main__":
    unittest.main()
