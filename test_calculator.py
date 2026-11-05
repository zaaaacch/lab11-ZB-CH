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

    # Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 5), 3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(4, 10), -6)
        self.assertEqual(subtract(-3, -3), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(8, 2), 3)
        self.assertAlmostEqual(logarithm(1, 10), 0)
        self.assertAlmostEqual(logarithm(100, 10), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(5, 1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()