import unittest

from counter import Counter
from multiplication_csd_2 import multiplication_csd_2


class test_multiplication_csd_2(unittest.TestCase):

    def test_5_x_7(self):
        result = multiplication_csd_2([1, 0, 1], [1, 0, 0, -1], Counter())
        self.assertEqual(
            "[ 0.  1.  0.  1. -1.  0. -1.]",
            str(result))

    def test_1_x_55(self):
        result = multiplication_csd_2([1], [1, 0, 0, -1, 0, 0, -1], Counter())
        self.assertEqual(
            "[ 0.  1.  0.  0. -1.  0.  0. -1.]",
            str(result))

    def test_minus3_x_3(self):
        result = multiplication_csd_2([-1, 0, 1], [1, 0, -1], Counter())
        self.assertEqual(
            "[ 0. -1.  1.  0.  0. -1.]",
            str(result))

    def test_10_x_6(self):
        result = multiplication_csd_2([1, 0, 1, 0], [1, 0, -1, 0], Counter())
        self.assertEqual(
            "[ 0.  1.  0.  0.  0. -1.  0.  0.]",
            str(result))

    def test_minus18_x_minus7(self):
        result = multiplication_csd_2([-1, 0, 0, -1, 0], [-1, 0, 0, 1], Counter())
        self.assertEqual(
            "[ 0.  1.  0.  0.  0.  0.  0. -1.  0.]",
            str(result))

    def test_5_x_5(self):
        result = multiplication_csd_2([1, 0, 1], [1, 0, 1], Counter())
        self.assertEqual(
            "[0. 1. 1. 0. 0. 1.]",
            str(result))

    def test_5_x_minus10(self):
        result = multiplication_csd_2([1, 0, 1], [-1, 0, -1, 0], Counter())
        self.assertEqual(
            "[ 0. -1. -1.  0.  0. -1.  0.]",
            str(result))


if __name__ == '__main__':
    unittest.main()
