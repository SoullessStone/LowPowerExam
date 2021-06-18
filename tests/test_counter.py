import unittest

from counter import Counter


class test_counter(unittest.TestCase):

    def test_count(self):
        sut = Counter()
        sut.count()
        sut.count()
        sut.count()
        self.assertEqual(3, sut.countValue)

    def test_countOtherValue(self):
        sut = Counter()
        sut.countOtherValue(4)
        self.assertEqual(4, sut.countValue)

    def test_no_interference(self):
        sut = Counter()
        sut2 = Counter()
        sut.countOtherValue(4)
        self.assertEqual(4, sut.countValue)
        self.assertEqual(0, sut2.countValue)


if __name__ == '__main__':
    unittest.main()
