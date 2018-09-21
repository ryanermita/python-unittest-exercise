import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = Calculator.add(1, 1)
        self.assertEqual(2, result)

    def test_subtract(self):
        result = Calculator.subtract(5, 3)
        self.assertEqual(2, result)

    def test_multiply(self):
        result = Calculator.multiply(2, 3)
        self.assertEqual(6, result)

    def test_divide(self):
        result = Calculator.divide(15, 5)
        self.assertEqual(3, result)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as cm:
            Calculator.divide(1, 0)
        self.assertEqual("Can not divide by zero!", str(cm.exception))
