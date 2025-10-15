from tokenizer import tokenize
from calculator_error import CalculatorError
from stack import RPNStack


class Parser:
    """Парсер математических выражений введеных в польской обратной нотации"""

    def __init__(self) -> None:
        self.stack = RPNStack()

    def parse(self, expression: str) -> float:
        """
        Парсинг выражения
        """
        self.stack.clear()

        try:
            tokens = tokenize(expression)
        except CalculatorError:
            raise CalculatorError("Ошибка ввода")

        brackets = []
        previous_token = None
        operators = False
        numbers_count = 0

        for i, (token_type, token_value) in enumerate(tokens):
            if token_type == "EOF":
                break
            if token_type == "NUM":
                numbers_count += 1
            elif token_type in self.stack.operators and token_type not in ['(', ')']:
                operators = True

            if token_type == '(':
                brackets.append(('(', i))
            elif token_type == ')':
                if not brackets:
                    raise CalculatorError("Ошибка скобки")
                if previous_token and previous_token[0] == '(':
                    raise CalculatorError("Пустые скобки")
                brackets.pop()

            previous_token = (token_type, token_value)

        if brackets:
            raise CalculatorError("Ошибка скобки")

        if numbers_count > 0 and not operators:
            raise CalculatorError("Нет операндов")

        for token_type, token_value in tokens:
            if token_type == "END":
                break
            if token_type == "NUM":
                self.stack.push(token_value)
            elif token_type in self.stack.operators:
                self.stack.apply_operator(token_type)

        return self.stack.get_result()
