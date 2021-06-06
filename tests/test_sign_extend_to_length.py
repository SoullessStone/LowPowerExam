import unittest

from sign_extend_to_length import sign_extend_to_length


class test_sign_extend_to_length(unittest.TestCase):

    def test_positive(self):
        result = sign_extend_to_length([0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1], 32)
        self.assertEqual(
            "[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1]",
            str(result))

    def test_negative(self):
        result = sign_extend_to_length([1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1], 32)
        self.assertEqual(
            "[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1]",
            str(result))

    def test_xbit(self):
        result = sign_extend_to_length([1, 0, 0, 1], 8)
        self.assertEqual(
            "[1, 1, 1, 1, 1, 0, 0, 1]",
            str(result))


if __name__ == '__main__':
    unittest.main()
