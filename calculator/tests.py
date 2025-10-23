import unittest
from pkg.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_evaluations(self):
        test_cases = [
            ("3 + 5", 8),
            ("10 - 4", 6),
            ("3 * 4", 12),
            ("10 / 2", 5),
            ("3 * 4 + 5", 17),
            ("2 * 3 - 8 / 2 + 5", 7),
        ]
        for expression, expected_result in test_cases:
            with self.subTest(expression=expression):
                result = self.calculator.evaluate(expression)
                self.assertEqual(result, expected_result)

    def test_empty_expression(self):
        result = self.calculator.evaluate("")
        self.assertIsNone(result)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("$ 3 5")

    def test_not_enough_operands(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("+ 3")

    def test_negative_numbers(self):
        test_cases = [
            ("5 + -3", 2),
            ("-5 + 3", -2),
            ("-5 - -3", -2),
            ("10 * -2", -20),
            ("-10 / 2", -5),
            ("2 * -3 + 5", -1),
        ]
        for expression, expected_result in test_cases:
            with self.subTest(expression=expression):
                result = self.calculator.evaluate(expression)
                self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
