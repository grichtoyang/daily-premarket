import unittest

from scripts.v9_pro_builder import classify_spot_institutions


class SpotInstitutionClassificationTests(unittest.TestCase):
    def test_all_positive(self):
        self.assertEqual(classify_spot_institutions([10, 20, 30]), "三法人現貨同向買超")

    def test_all_negative(self):
        self.assertEqual(classify_spot_institutions([-10, -20, -30]), "三法人現貨同向賣超")

    def test_mixed_directions(self):
        self.assertEqual(classify_spot_institutions([-10, 20, -30]), "現貨三法人方向分歧")

    def test_zero_is_not_all_buy_or_all_sell(self):
        self.assertEqual(classify_spot_institutions([10, 0, 30]), "現貨三法人方向分歧")

    def test_missing_one_value(self):
        self.assertEqual(classify_spot_institutions([-10, None, -30]), "現貨三法人資料不足，不能完整判定方向")

    def test_wrong_number_of_values(self):
        self.assertEqual(classify_spot_institutions([10, 20]), "現貨三法人資料不足，不能完整判定方向")


if __name__ == "__main__":
    unittest.main()
