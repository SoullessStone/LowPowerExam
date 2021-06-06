import unittest

from pad_binary import pad_binary


class test_pad_binary(unittest.TestCase):

    def test_pad(self):
        result = pad_binary([0, 1, 0, 0, 1, 1], 10)
        self.assertEqual("[0, 0, 0, 0, 0, 1, 0, 0, 1, 1]", str(result))

    def test_already_longer(self):
        result = pad_binary([0, 1, 0, 0, 1, 1], 4)
        self.assertEqual("[0, 1, 0, 0, 1, 1]", str(result))


if __name__ == '__main__':
    unittest.main()
