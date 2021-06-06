import unittest

from invert_csd import invert_csd


class test_invert_csd(unittest.TestCase):

    def test_a(self):
        result = invert_csd([0, 1, 0, 0, -1, 0])
        self.assertEqual("[ 0. -1.  0.  0.  1.  0.]", str(result))


if __name__ == '__main__':
    unittest.main()
