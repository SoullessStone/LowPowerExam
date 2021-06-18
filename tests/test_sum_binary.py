import unittest

from counter import Counter
from sum_binary import sum_binary


class test_sum_binary(unittest.TestCase):

    def test_a(self):
        counter = Counter()
        result = sum_binary([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], counter)
        self.assertEqual("[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]", str(result))
        self.assertEqual(2, counter.countValue)

    def test_b(self):
        counter = Counter()
        result = sum_binary([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], counter)
        self.assertEqual("[1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]", str(result))
        self.assertEqual(17, counter.countValue)

    def test_c(self):
        counter = Counter()
        result = sum_binary([0, 1, 1, 1, 1], [0, 0, 0, 0, 1], counter)
        self.assertEqual("[0. 1. 0. 0. 0. 0.]", str(result))
        self.assertEqual(5, counter.countValue)

    def test_d(self):
        counter = Counter()
        result = sum_binary([0, 1, 0, 1, 1], [0, 0, 0, 0, 1], counter)
        self.assertEqual("[0. 0. 1. 1. 0. 0.]", str(result))
        self.assertEqual(4, counter.countValue)

    def test_unequal_length_a(self):
        counter = Counter()
        result = sum_binary([1, 1, 1], [0, 1], counter)
        self.assertEqual("[1. 0. 0. 0.]", str(result))
        self.assertEqual(4, counter.countValue)

    def test_unequal_length_b(self):
        counter = Counter()
        result = sum_binary([1, 0], [1, 0, 0], counter)
        self.assertEqual("[0. 1. 1. 0.]", str(result))
        self.assertEqual(2, counter.countValue)


if __name__ == '__main__':
    unittest.main()
