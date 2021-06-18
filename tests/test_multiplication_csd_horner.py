import unittest

from counter import Counter
from multiplication_csd_horner import multiplication_csd_horner


class test_multiplication_csd_horner(unittest.TestCase):

    def test_41_x_441(self):
        result = multiplication_csd_horner([0, 1, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 1, 1, 0, 0, 1], Counter())
        self.assertEqual(
            "[0. 0. 1. 0. 0. 0. 1. 1. 0. 1. 0. 1. 0. 0. 0. 0. 1.]",
            str(result))

    def test_41_x_minus441(self):
        result = multiplication_csd_horner([0, 1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0, 0, 1, 1, 1], Counter())
        self.assertEqual(
            "[1. 1. 0. 1. 1. 1. 0. 0. 1. 0. 1. 0. 1. 1. 1. 1. 1.]",
            str(result))

    def test_557_x_234(self):
        result = multiplication_csd_horner([0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 1, 0], Counter())
        self.assertEqual(
            "[0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 0. 1. 0. 0. 1. 0. 0. 0. 1. 0.]",
            str(result))

    def test_minus41_x_441(self):
        result = multiplication_csd_horner([1, 0, 1, 0, 1, 1, 1], [0, 1, 1, 0, 1, 1, 1, 0, 0, 1], Counter())
        self.assertEqual(
            "[1. 1. 0. 1. 1. 1. 0. 0. 1. 0. 1. 0. 1. 1. 1. 1. 1.]",
            str(result))

    def test_72_x_90(self):
        result = multiplication_csd_horner([0, 1, 0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 1, 0, 1, 0], Counter())
        self.assertEqual(
            "[0. 0. 0. 1. 1. 0. 0. 1. 0. 1. 0. 1. 0. 0. 0. 0.]",
            str(result))

    def test_2541_x_4015(self):
        result = multiplication_csd_horner([0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
                                           [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1], Counter())
        self.assertEqual(
            "[0. 0. 1. 0. 0. 1. 1. 0. 1. 1. 1. 0. 1. 0. 1. 1. 0. 0. 0. 0. 0. 0. 0. 0.\n 1. 1.]",
            str(result))

    def test_minus1_x_23979(self):
        result = multiplication_csd_horner([1, 1, 1], [0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1], Counter())
        self.assertEqual(
            "[1. 1. 1. 1. 0. 1. 0. 0. 0. 1. 0. 0. 1. 0. 1. 0. 1. 0. 1.]",
            str(result))

    def test_minus23_x_77(self):
        result = multiplication_csd_horner([1, 1, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 1, 1, 0, 1], Counter())
        self.assertEqual(
            "[1. 1. 1. 1. 1. 0. 0. 1. 0. 0. 0. 1. 0. 1. 0. 1.]",
            str(result))

    def test_77_x_minus23(self):
        result = multiplication_csd_horner([0, 1, 0, 0, 1, 1, 0, 1], [1, 1, 1, 0, 1, 0, 0, 1], Counter())
        self.assertEqual(
            "[1. 1. 1. 1. 1. 0. 0. 1. 0. 0. 0. 1. 0. 1. 0. 1.]",
            str(result))

    def test_minus1_x_1(self):
        result = multiplication_csd_horner([1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1], Counter())
        self.assertEqual(
            "[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]",
            str(result))

    def test_1_x_minus1(self):
        result = multiplication_csd_horner([0, 0, 1], [1, 1, 1, 1], Counter())
        self.assertEqual(
            "[1. 1. 1. 1. 1. 1. 1.]",
            str(result))

    def test_minus7_x_5(self):
        result = multiplication_csd_horner([1, 0, 0, 1], [0, 1, 0, 1], Counter())
        self.assertEqual(
            "[1. 1. 0. 1. 1. 1. 0. 1.]",
            str(result))

    def test_5_x_minus7(self):
        result = multiplication_csd_horner([0, 1, 0, 1], [1, 0, 0, 1], Counter())
        self.assertEqual(
            "[1. 1. 0. 1. 1. 1. 0. 1.]",
            str(result))


if __name__ == '__main__':
    unittest.main()
