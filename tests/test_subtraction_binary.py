import unittest

from counter import Counter
from subtraction_binary import subtraction_binary


# testcases http://sandbox.mc.edu/~bennet/cs110/pm/sub.html
class test_subtraction_binary(unittest.TestCase):

    def test_a(self):
        result = subtraction_binary([1, 0, 1, 1, 0, 1, 1], [1, 0, 0, 1, 0], Counter())
        self.assertEqual("[1, 0, 0, 1, 0, 0, 1]", str(result))

    def test_b(self):
        result = subtraction_binary([1, 0, 0, 0, 1, 0, 1], [1, 0, 1, 1, 0, 0], Counter())
        self.assertEqual("[0, 0, 1, 1, 0, 0, 1]", str(result))

    def test_c(self):
        result = subtraction_binary([1, 0, 0, 0, 1, 0, 1, 1, 0], [1, 1, 1, 1, 0, 1, 0], Counter())
        self.assertEqual("[0, 1, 0, 0, 1, 1, 1, 0, 0]", str(result))

    def test_d(self):
        result = subtraction_binary([1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1], Counter())
        self.assertEqual("[0, 0, 0, 1, 1, 0]", str(result))

    def test_e(self):
        result = subtraction_binary([1, 1, 1, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1], Counter())
        self.assertEqual("[0, 0, 1, 1, 1, 1, 1]", str(result))

    def test_f(self):
        result = subtraction_binary([0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1], Counter())
        self.assertEqual("[0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1]", str(result))

    def test_g(self):
        result = subtraction_binary([0, 0, 0, 1], [0, 0, 1, 0], Counter())
        self.assertEqual("[1, 1, 1, 1]", str(result))


if __name__ == '__main__':
    unittest.main()
