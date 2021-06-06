import unittest

from multiplication_csd_horner import multiplication_csd_horner


class test_multiplication_csd_horner(unittest.TestCase):

    def test_41_x_441(self):
        result = multiplication_csd_horner([0, 1, 0, 1, 0, 0, 1],
                                           [0, 1, 1, 0, 1, 1, 1, 0, 0, 1])
        self.assertEqual(
            "[1. 0. 0. 0. 1. 1. 0. 1. 0. 1. 0. 0. 0. 0. 1.]",
            str(result))

    def test_557_x_234(self):
        result = multiplication_csd_horner([0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
                                           [0, 1, 1, 1, 0, 1, 0, 1, 0])
        self.assertEqual(
            "[0. 1. 1. 1. 1. 1. 1. 1. 0. 1. 0. 0. 1. 0. 0. 0. 1. 0.]",
            str(result))

    def test_minus41_x_441(self):
        result = multiplication_csd_horner([1, 0, 1, 0, 1, 1, 1],
                                           [0, 1, 1, 0, 1, 1, 1, 0, 0, 1])
        self.assertEqual(
            "[1. 0. 1. 1. 1. 0. 0. 1. 0. 1. 0. 1. 1. 1. 1. 1.]",
            str(result))


if __name__ == '__main__':
    unittest.main()
