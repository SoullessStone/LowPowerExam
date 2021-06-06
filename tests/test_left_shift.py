import unittest

from left_shift import left_shift


class test_left_shift(unittest.TestCase):

    def test_0(self):
        result = left_shift([0, 1, 0, 0, 1, 1], 0)
        self.assertEqual("[0. 1. 0. 0. 1. 1.]", str(result))

    def test_1(self):
        result = left_shift([0, 1, 0, 0, 1, 1], 1)
        self.assertEqual("[0. 1. 0. 0. 1. 1. 0.]", str(result))

    def test_2(self):
        result = left_shift([0, 1, 0, 0, 1, 1], 2)
        self.assertEqual("[0. 1. 0. 0. 1. 1. 0. 0.]", str(result))


if __name__ == '__main__':
    unittest.main()
