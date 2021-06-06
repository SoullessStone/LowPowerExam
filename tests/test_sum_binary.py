import unittest

from sum_binary import sum_binary


class test_sum_binary(unittest.TestCase):

    def test_a(self):
        result = sum_binary([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        self.assertEqual("[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]", str(result))

    def test_b(self):
        result = sum_binary([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        self.assertEqual("[1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]", str(result))

    def test_c(self):
        result = sum_binary([0, 1, 1, 1, 1],
                            [0, 0, 0, 0, 1])
        self.assertEqual("[0. 1. 0. 0. 0. 0.]", str(result))

    def test_d(self):
        result = sum_binary([0, 1, 0, 1, 1],
                            [0, 0, 0, 0, 1])
        self.assertEqual("[0. 0. 1. 1. 0. 0.]", str(result))

    def test_unequal_length_a(self):
        result = sum_binary([1, 1, 1],
                            [0, 1])
        self.assertEqual("[1. 0. 0. 0.]", str(result))

    def test_unequal_length_b(self):
        result = sum_binary([1, 0],
                            [1, 0, 0])
        self.assertEqual("[0. 1. 1. 0.]", str(result))


if __name__ == '__main__':
    unittest.main()
