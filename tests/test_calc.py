import unittest

from src.expression_parser import calculate_expression


class TestExpressions(unittest.TestCase):
    """Тесты выражений"""

    def test_basic_operations(self):
        self.assertEqual(calculate_expression("2 2 +"), 4.0)
        self.assertEqual(calculate_expression("~5 3 +"), -2.0)
        self.assertEqual(calculate_expression("$5 3 +"), 8.0)
        self.assertEqual(calculate_expression("0 5 +"), 5.0)
        self.assertEqual(calculate_expression("~2 ~2 -"), 0.0)
        self.assertEqual(calculate_expression("10 4 -"), 6.0)
        self.assertEqual(calculate_expression("3 7 *"), 21.0)
        self.assertEqual(calculate_expression("1 1 *"), 1.0)
        self.assertEqual(calculate_expression("15 3 /"), 5.0)
        self.assertEqual(calculate_expression("17 5 //"), 3.0)
        self.assertEqual(calculate_expression("17 5 %"), 2.0)
        self.assertEqual(calculate_expression("2 10 **"), 1024.0)

    def test_complex_expressions(self):
        self.assertEqual(calculate_expression("2 3 4 * +"), 14.0)
        self.assertEqual(calculate_expression("2 3 4 * + 5 2 / -"), 11.5)
        self.assertEqual(calculate_expression("2 3 + 4 1 - * 10 3 // +"), 18.0)

    def test_with_brackets(self):
        self.assertEqual(calculate_expression("(2 ~2 *)"), -4.0)
        self.assertEqual(calculate_expression("(2 3 *)(4 5 -)*"), -6.0)
        self.assertEqual(calculate_expression("((4 2 +) (3 1 -) ** 5) // 1 +"), 8.0)


if __name__ == "__main__":
    unittest.main()
