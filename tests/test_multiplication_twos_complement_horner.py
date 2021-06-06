import unittest

from multiplication_twos_complement_horner import multiplication_twos_complement_horner


class test_multiplication_twos_complement_horner(unittest.TestCase):

    def test_72_x_90(self):
        result = multiplication_twos_complement_horner([0, 1, 0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 1, 0, 1, 0])
        self.assertEqual(
            "[1. 1. 0. 0. 1. 0. 1. 0. 1. 0. 0. 0. 0.]",
            str(result))

    def test_2541_x_4015(self):
        result = multiplication_twos_complement_horner([0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
                                                       [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1])
        self.assertEqual(
            "[1. 0. 0. 1. 1. 0. 1. 1. 1. 0. 1. 0. 1. 1. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1.]",
            str(result))

    # todo: wenn links negativ ist, hat es noch probleme
    def test_minus1_x_23979(self):
        result = multiplication_twos_complement_horner([1, 1, 1],
                                                       [0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1])
        self.assertEqual(
            "",
            str(result))

    def test_minus23_x_77(self):
        result = multiplication_twos_complement_horner([1, 1, 1, 0, 1, 0, 0, 1],
                                                       [0, 1, 0, 0, 1, 1, 0, 1])
        self.assertEqual(
            "",
            str(result))

    def test_77_x_minus23(self):
        result = multiplication_twos_complement_horner([0, 1, 0, 0, 1, 1, 0, 1],
                                                       [1, 1, 1, 0, 1, 0, 0, 1])
        self.assertEqual(
            "[1. 1. 1. 1. 0. 0. 1. 0. 0. 0. 1. 0. 1. 0. 1.]",
            str(result))

    def test_minus1_x_1(self):
        result = multiplication_twos_complement_horner([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        self.assertEqual(
            "[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]",
            str(result))

    def test_1_x_minus1(self):
        result = multiplication_twos_complement_horner([0, 0, 1],
                                                       [1, 1, 1, 1])
        self.assertEqual(
            "[1. 1. 1. 1. 1. 1.]",
            str(result))

    def test_minus7_x_5(self):
        result = multiplication_twos_complement_horner([1, 0, 0, 1],
                                                       [0, 1, 0, 1])
        self.assertEqual(
            "100100",
            str(result))

    def test_5_x_minus7(self):
        result = multiplication_twos_complement_horner([0, 1, 0, 1],
                                                       [1, 0, 0, 1])
        self.assertEqual(
            "[1. 0. 1. 1. 1. 0. 1.]",
            str(result))


if __name__ == '__main__':
    unittest.main()
