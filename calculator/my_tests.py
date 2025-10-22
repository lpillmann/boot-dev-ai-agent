
import unittest
from pkg.calculator import Calculator

class MyCalculatorTests(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.evaluate("10 / 0")

    def test_parentheses(self):
        result = self.calculator.evaluate("( 3 + 5 ) * 2")
        self.assertEqual(result, 16)

    def test_float_result(self):
        result = self.calculator.evaluate("7 / 2")
        self.assertEqual(result, 3.5)

    def test_negative_numbers(self):
        result = self.calculator.evaluate("-5 + 10")
        self.assertEqual(result, 5)

    def test_multiple_operators_same_precedence(self):
        result = self.calculator.evaluate("10 - 5 + 2")
        self.assertEqual(result, 7)

    def test_leading_or_trailing_spaces(self):
        result = self.calculator.evaluate("  1 + 2   ")
        self.assertEqual(result, 3)

    def test_multiple_spaces_between_tokens(self):
        result = self.calculator.evaluate("1   +   2")
        self.assertEqual(result, 3)

    def test_complex_expression_with_floats(self):
        result = self.calculator.evaluate("3.5 + 2 * 1.5 - 0.5")
        self.assertEqual(result, 6.0)

    def test_single_number(self):
        result = self.calculator.evaluate("42")
        self.assertEqual(result, 42)

    def test_single_negative_number(self):
        result = self.calculator.evaluate("-42")
        self.assertEqual(result, -42)

    def test_very_long_expression(self):
        expression = "1 " + "+ 1 " * 100
        result = self.calculator.evaluate(expression)
        self.assertEqual(result, 101)

if __name__ == '__main__':
    unittest.main()
