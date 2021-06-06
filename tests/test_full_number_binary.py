import unittest

from full_number_binary import full_number_binary


class test_full_number_binary(unittest.TestCase):

    def test_0(self):
        test, bla = full_number_binary(0, 16)
        self.assertEqual("[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]", str(test))

    def test_1(self):
        test, bla = full_number_binary(1, 16)
        self.assertEqual("[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]", str(test))

    def test_max(self):
        test, bla = full_number_binary(2 ** 17 - 1, 16)
        self.assertEqual("[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]", str(test))


if __name__ == '__main__':
    unittest.main()
