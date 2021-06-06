import unittest

from left_trim import left_trim


class test_left_trim(unittest.TestCase):

    def test_0(self):
        result = left_trim([0, 1, 0, 0, 1, 1])
        self.assertEqual("[1, 0, 0, 1, 1]", str(result))

    def test_2x0(self):
        result = left_trim([0, 0, 1, 0, 0, 1, 1])
        self.assertEqual("[1, 0, 0, 1, 1]", str(result))

    def test_no_trim1(self):
        result = left_trim([1, 0, 0, 1, 1])
        self.assertEqual("[1, 0, 0, 1, 1]", str(result))

    def test_0_minus1(self):
        result = left_trim([0, -1, 0, 0, 1, 1])
        self.assertEqual("[-1, 0, 0, 1, 1]", str(result))

    def test_2x0_minus1(self):
        result = left_trim([0, 0, -1, 0, 0, 1, 1])
        self.assertEqual("[-1, 0, 0, 1, 1]", str(result))

    def test_no_trim1_minus1(self):
        result = left_trim([-1, 0, 0, 1, 1])
        self.assertEqual("[-1, 0, 0, 1, 1]", str(result))

    def test_no_trimMinus1(self):
        result = left_trim([-1, 0, 0, 1, 1])
        self.assertEqual("[-1, 0, 0, 1, 1]", str(result))


if __name__ == '__main__':
    unittest.main()
