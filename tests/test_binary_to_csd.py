import unittest

from binary_to_csd import binary_to_csd
from counter import Counter


class test_binary_to_csd(unittest.TestCase):

    # tests according to: https://www.allaboutcircuits.com/technical-articles/an-introduction-to-canonical-signed-digit-representation/
    def test_a(self):
        result = binary_to_csd([0, 1, 0, 1, 1, 1, 0, 1], Counter())
        self.assertEqual("[ 1  0 -1  0  0 -1  0  1]", str(result))

    def test_87(self):
        result = binary_to_csd([0, 1, 0, 1, 0, 1, 1, 1], Counter())
        self.assertEqual("[ 1  0 -1  0 -1  0  0 -1]", str(result))

    def test_minus41(self):
        result = binary_to_csd([1, 0, 1, 0, 1, 1, 1], Counter())
        self.assertEqual("[ 0. -1.  0. -1.  0.  0. -1.]", str(result))

    def test_441(self):
        result = binary_to_csd([0, 1, 1, 0, 1, 1, 1, 0, 0, 1], Counter())
        self.assertEqual("[ 1  0  0 -1  0  0 -1  0  0  1]", str(result))

    def test_minus441(self):
        result = binary_to_csd([1, 0, 0, 1, 0, 0, 0, 1, 1, 1], Counter())
        self.assertEqual("[-1.  0.  0.  1.  0.  0.  1.  0.  0. -1.]", str(result))


if __name__ == '__main__':
    unittest.main()
