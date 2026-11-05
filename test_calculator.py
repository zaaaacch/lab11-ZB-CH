# https://github.com/zaaaacch/lab11-ZB-CH
# Partner 1: Zach Beattie
# Partner 2: Cooper Hayes

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    # Partner 1
    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(10, 2), 20)
        self.assertEqual(mul(-5, 2), -10)

    def test_divide(self):
        self.assertAlmostEqual(div(2, 10), 5)
        self.assertAlmostEqual(div(50, 500), 10)
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)
        self.assertAlmostEqual(hypotenuse(0, 0), 0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(0), 0)
        with self.assertRaises(ValueError):
            square_root(-1)

    # Partner 2 tests go here after pulling into labpartner2.


# Do not touch this
if __name__ == "__main__":
    unittest.main()