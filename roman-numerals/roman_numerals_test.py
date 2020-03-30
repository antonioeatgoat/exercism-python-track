import unittest

from roman_numerals import roman

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0
class RomanNumeralsTest(unittest.TestCase):
    def test_1_is_a_single_i(self):
        self.assertEqual("I", roman(1))

    def test_2_is_two_i_s(self):
        self.assertEqual("II", roman(2))

    def test_3_is_three_i_s(self):
        self.assertEqual("III", roman(3))

    def test_4_being_5_1_is_iv(self):
        self.assertEqual("IV", roman(4))

    def test_5_is_a_single_v(self):
        self.assertEqual("V", roman(5))

    def test_6_being_5_1_is_vi(self):
        self.assertEqual("VI", roman(6))

    def test_9_being_10_1_is_ix(self):
        self.assertEqual("IX", roman(9))

    def test_20_is_two_x_s(self):
        self.assertEqual("XXVII", roman(27))

    def test_48_is_not_50_2_but_rather_40_8(self):
        self.assertEqual("XLVIII", roman(48))

    def test_49_is_not_40_5_4_but_rather_50_10_10_1(self):
        self.assertEqual("XLIX", roman(49))

    def test_50_is_a_single_l(self):
        self.assertEqual("LIX", roman(59))

    def test_90_being_100_10_is_xc(self):
        self.assertEqual("XCIII", roman(93))

    def test_100_is_a_single_c(self):
        self.assertEqual("CXLI", roman(141))

    def test_60_being_50_10_is_lx(self):
        self.assertEqual("CLXIII", roman(163))

    def test_400_being_500_100_is_cd(self):
        self.assertEqual("CDII", roman(402))

    def test_500_is_a_single_d(self):
        self.assertEqual("DLXXV", roman(575))

    def test_900_being_1000_100_is_cm(self):
        self.assertEqual("CMXI", roman(911))

    def test_1000_is_a_single_m(self):
        self.assertEqual("MXXIV", roman(1024))

    def test_3000_is_three_m_s(self):
        self.assertEqual("MMM", roman(3000))


if __name__ == "__main__":
    unittest.main()
