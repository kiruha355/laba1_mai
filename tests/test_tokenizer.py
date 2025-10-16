import unittest

from src.tokenizer import tokenize
from src.calculator_error import CalculatorError


class TestTokenizer(unittest.TestCase):
    """Тесты токенезации"""
    def test_tokenize_numbers(self):
        self.assertEqual(tokenize("123"), [("NUM", 123.0), ("END", None)])
        self.assertEqual(tokenize("~1"), [("NUM", -1.0), ("END", None)])
        self.assertEqual(tokenize("12.30"), [("NUM", 12.30), ("END", None)])

    def test_tokenize_operators(self):
        self.assertEqual(tokenize("+"), [("+", None), ("END", None)])
        self.assertEqual(tokenize("**"), [("**", None), ("END", None)])

    def test_tokenize_expression(self):
        tokens = tokenize("1 + 2 * ~3")
        expected = [("NUM", 1.0), ("+", None), ("NUM", 2.0),
                    ("*", None), ("NUM", -3.0), ("END", None)]
        self.assertEqual(tokens, expected)

    def test_tokenize_invalid_token(self):
        with self.assertRaises(CalculatorError) as context:
            tokenize("2 meow 2")
        self.assertEqual(str(context.exception), "Ошибка ввода")


if __name__ == "__main__":
    unittest.main()
