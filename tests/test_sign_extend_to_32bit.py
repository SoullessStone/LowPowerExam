import unittest

from sign_extend_to_32bit import sign_extend_to_32bit


class test_sign_extend_to_32bit(unittest.TestCase):

    def test_positive(self):
        result = sign_extend_to_32bit([0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1])
        self.assertEqual(
            "[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1]",
            str(result))

    def test_negative(self):
        result = sign_extend_to_32bit([1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1])
        self.assertEqual(
            "[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1]",
            str(result))


if __name__ == '__main__':
    unittest.main()
