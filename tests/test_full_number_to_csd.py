import unittest

from full_number_to_csd import full_number_to_csd


class test_full_number_to_csd(unittest.TestCase):

    def test_a(self):
        result = full_number_to_csd(1898)  # 11101101010
        self.assertEqual("[ 0.  0.  0.  0.  0.  1.  0.  0.  0. -1.  0. -1.  0.  1.  0.  1.  0.]", str(result))

    def test_minusA(self):
        result = full_number_to_csd(-1898)  # 11101101010
        self.assertEqual("[ 0.  0.  0.  0.  0. -1.  0.  0.  0.  1.  0.  1.  0. -1.  0. -1.  0.]", str(result))

    def test_30(self):
        result = full_number_to_csd(30)
        self.assertEqual("[ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1.  0.  0.  0. -1.  0.]", str(result))

    def test_41(self):
        result = full_number_to_csd(41)
        self.assertEqual("[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 1. 0. 0. 1.]", str(result))

    def test_30411(self):
        result = full_number_to_csd(30411)
        self.assertEqual("[ 0.  1.  0.  0.  0. -1.  0.  0. -1.  0. -1.  0.  1.  0. -1.  0. -1.]", str(result))


if __name__ == '__main__':
    unittest.main()
