from .calculator_error import CalculatorError


class RPNStack:
    """
    Стек, реализованный по принципу Lost In First Out
    """

    def __init__(self) -> None:
        """
        1.Создаем пустой стек
        2.Создаем слвоарь операций и в значения указываем кортеж: (приоритетность , что выполняет операнд)
        """
        self.stack: list[float] = []
        self.operators = {
            '(': (0, None),
            ')': (0, None),
            '+': (1, lambda a, b: a + b),
            '-': (1, lambda a, b: a - b),
            '*': (2, lambda a, b: a * b),
            '/': (2, lambda a, b: a / b if b != 0 else self._error("Деление на ноль")),
            '//': (2, lambda a, b: a // b if b != 0 else self._error("Деление на ноль")),
            '%': (2, lambda a, b: a % b if b != 0 else self._error("Деление на ноль")),
            '**': (3, lambda a, b: a ** b),
        }

    def _error(self, message: str) -> None:  # ← Добавил этот метод
        """
        Выброс ошибок
        """
        raise CalculatorError(message)

    def push(self, value: float) -> None:
        """
        Добавить значение в стек
        """
        self.stack.append(value)

    def pop(self) -> float:
        """
        Извлечь значение из стека
        """
        if not self.stack:
            raise CalculatorError("Ошибка ввода")
        return self.stack.pop()

    def check_operand(self, a: float, b: float, operator: str) -> None:
        """
        Проверка для операций % и //
        """
        if operator in ['%', '//']:
            if not a.is_integer() or not b.is_integer():
                raise CalculatorError(f"Операция '{operator}' допустима только для целых чисел")

    def apply_operator(self, operator: str) -> None:
        """
        Игнорируем скобки и перенаправляет на выполненнии операции.Проверяем, чтобы введеных чисел было хотя бы два.
        """
        if operator in ['(', ')']:
            return
        if len(self.stack) < 2:
            raise CalculatorError("Недостаточно значений/операндов")

        b = self.pop()
        a = self.pop()

        result = self.do_operation(operator, a, b)
        self.push(result)
        self.check_operand(a, b, operator)

    def do_operation(self, operator: str, a: float, b: float) -> float:
        """
        Выполнение математической операции
        """
        match operator:
            case '+':
                return a + b
            case '-':
                return a - b
            case '*':
                return a * b
            case '/':
                if b == 0:
                    raise CalculatorError("Деление на ноль")
                return a / b
            case '//':
                if b == 0:
                    raise CalculatorError("Деление на ноль")
                return a // b
            case '%':
                if b == 0:
                    raise CalculatorError("Деление на ноль")
                return a % b
            case '**':
                return a ** b
            case _:
                raise CalculatorError("Ошибка ввода")

    def get_result(self) -> float:
        """
        Получить результат из стека
        """
        return self.stack[0]

    def clear(self) -> None:
        """
        Очистить стек
        """
        self.stack = []
