import unittest
from calculator import Calculator

class testCalculatorClass(unittest.TestCase):

    def test_add_int_with_int(self):
        func = Calculator.add(1, 2)

        self.assertEqual(func, 3)

    def test_add_int_with_float(self):
        func = Calculator.add(1, 2.2)

        self.assertEqual(func, 3.2)

    def test_add_int_with_str(self):
        with self.assertRaises(TypeError) as cm:
            Calculator.add(1, "2")

        self.assertEqual(str(cm.exception), "Invalid Value")

    def test_divide_int_with_int(self):
        func = Calculator.divide(1, 2)
        self.assertEqual(func, 0.5)

    def test_divide_int_with_float(self):
        func = Calculator.divide(21, 2.5)
        self.assertEqual(func, 8.4)

    def test_divide_int_with_0(self):
        with self.assertRaises(ValueError) as cm:
            Calculator.divide(5, 0)

        self.assertEqual(str(cm.exception), "Can not divide by zero!")

    def test_divide_int_with_str(self):
        with self.assertRaises(TypeError) as cm:
            Calculator.divide(1, "2")

        self.assertEqual(str(cm.exception), "Invalid Value")

    def test_divide_where_result_is_infinite_num(self):
        func = Calculator.divide(10, 3)

        self.assertAlmostEqual(func, 3.33333, places=5)
