import unittest

from src.calculator_error import CalculatorError
from src.expression_parser import calculate_expression


class TestErrors(unittest.TestCase):
    """Тесты по ошибкам"""

    def test_error_empty_input(self):
        with self.assertRaises(CalculatorError) as context:
            calculate_expression("")
        self.assertEqual(str(context.exception), "Ошибка ввода")

    def test_error_division_by_zero(self):
        with self.assertRaises(CalculatorError) as context:
            calculate_expression("5 0 /")
        self.assertEqual(str(context.exception), "Деление на ноль")

    def test_error_floor_division_non_integer(self):
        with self.assertRaises(CalculatorError) as context:
            calculate_expression("5.5 2 //")
        self.assertEqual(str(context.exception), "Операция '//' допустима только для целых чисел")

    def test_error_modulo_non_integer(self):
        with self.assertRaises(CalculatorError) as context:
            calculate_expression("5 2.5 %")
        self.assertEqual(str(context.exception), "Операция '%' допустима только для целых чисел")

    def test_error_invalid_token(self):
        with self.assertRaises(CalculatorError) as context:
            calculate_expression("2 meow 2 meow")
        self.assertEqual(str(context.exception), "Ошибка ввода")

    def test_error_unmatched_bracket1(self):
        with self.assertRaises(CalculatorError) as context:
            calculate_expression("(2 + 2")
        self.assertEqual(str(context.exception), "Ошибка скобки")

    def test_error_unmatched_bracket2(self):
        with self.assertRaises(CalculatorError) as context:
            calculate_expression("2 + 2)")
        self.assertEqual(str(context.exception), "Ошибка скобки")

    def test_error_empty_brackets(self):
        with self.assertRaises(CalculatorError) as context:
            calculate_expression("()")
        self.assertEqual(str(context.exception), "Пустые скобки")

    def test_error_no_operators(self):
        with self.assertRaises(CalculatorError) as context:
            calculate_expression("2 3 4")
        self.assertEqual(str(context.exception), "Нет операндов")


if __name__ == "__main__":
    unittest.main()
