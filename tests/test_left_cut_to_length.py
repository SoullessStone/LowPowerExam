import unittest

from left_cut_to_length import left_cut_to_length


class test_left_cut_to_length(unittest.TestCase):

    def test_already_longer(self):
        result = left_cut_to_length([0, 1, 0, 0, 1, 1], 8)
        self.assertEqual("[0, 1, 0, 0, 1, 1]", str(result))

    def test_already_good(self):
        result = left_cut_to_length([0, 1, 0, 0, 1, 1], 6)
        self.assertEqual("[0, 1, 0, 0, 1, 1]", str(result))

    def test_cut(self):
        result = left_cut_to_length([0, 1, 0, 0, 1, 1], 4)
        self.assertEqual("[0, 0, 1, 1]", str(result))


if __name__ == '__main__':
    unittest.main()
