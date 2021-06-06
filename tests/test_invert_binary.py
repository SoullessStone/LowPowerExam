import unittest

from invert_binary import invert_binary


class test_invert_binary(unittest.TestCase):

    def test_a(self):
        result = invert_binary([0, 1, 1, 0, 1, 0])
        self.assertEqual("[1, 0, 0, 1, 0, 1]", str(result))

    def test_b(self):
        result = invert_binary([1, 1, 1, 1, 1, 1])
        self.assertEqual("[0, 0, 0, 0, 0, 0]", str(result))

    def test_c(self):
        result = invert_binary([0, 0, 0])
        self.assertEqual("[1, 1, 1]", str(result))


if __name__ == '__main__':
    unittest.main()
