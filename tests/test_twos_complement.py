import unittest

from twos_complement import twos_complement


class test_twos_complement(unittest.TestCase):

    def test_1(self):
        result = twos_complement(1)
        self.assertEqual("[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]", str(result))

    def test_max(self):
        result = twos_complement(2 ** 15 - 1)
        self.assertEqual("[0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]", str(result))

    def test_minus_1(self):
        result = twos_complement(-1)
        self.assertEqual("[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]", str(result))

    def test_minus_30(self):
        result = twos_complement(-30)
        self.assertEqual("[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 0. 0. 1. 0.]", str(result))

    def test_minus_min(self):
        result = twos_complement(-2 ** 15)
        self.assertEqual("[1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]", str(result))


if __name__ == '__main__':
    unittest.main()
