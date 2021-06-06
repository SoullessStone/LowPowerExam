import unittest

from multiplication_twos_complement import multiplication_twos_complement


class test_multiplication_twos_complement(unittest.TestCase):

    def test_one_x_anything(self):
        result = multiplication_twos_complement([1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
                                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        self.assertEqual(
            "[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 0. 1. 0. 0. 0. 0.\n 1. 1. 1. 0. 0. 0. 0. 1.]",
            str(result))

    def test_6_x_minus5(self):
        result = multiplication_twos_complement([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1])
        self.assertEqual(
            "[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.\n 1. 1. 1. 0. 0. 0. 1. 0.]",
            str(result))

    def test_minus2_x_minus1898(self):
        result = multiplication_twos_complement(
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0])

        self.assertEqual(
            "[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 1. 0.\n 1. 1. 0. 1. 0. 1. 0. 0.]",
            str(result))

    def test_6_x_minus7(self):
        result = multiplication_twos_complement(
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1])

        self.assertEqual(
            "[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.\n 1. 1. 0. 1. 0. 1. 1. 0.]",
            str(result))

    def test_minus4_x_3(self):
        result = multiplication_twos_complement(
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1])

        self.assertEqual(
            "[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.\n 1. 1. 1. 1. 0. 1. 0. 0.]",
            str(result))


if __name__ == '__main__':
    unittest.main()
