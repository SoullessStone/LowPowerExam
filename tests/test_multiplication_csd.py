import unittest

from multiplication_csd import multiplication_csd


class test_multiplication_csd(unittest.TestCase):

    def test_5_x_7(self):
        result = multiplication_csd([1, 0, 1],
                                    [1, 0, 0, -1])
        self.assertEqual(
            "[0. 1. 0. 0. 0. 1. 1.]",
            str(result))

    def test_1_x_55(self):
        result = multiplication_csd([1],
                                    [1, 0, 0, -1, 0, 0, -1])
        self.assertEqual(
            "[0. 0. 1. 1. 0. 1. 1. 1.]",  # 55 in binär
            str(result))

    # TODO mehr tests: negativzahlen, -1 in a (nicht nur b)


if __name__ == '__main__':
    unittest.main()
