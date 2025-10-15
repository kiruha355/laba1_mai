from expression_parser import Parser
from calculator_error import CalculatorError


def main() -> None:
    """
    Основная функция работы калькулятора
    """
    parser = Parser()

    while True:
        try:
            expression = input("\nВведите выражение: ").strip()

            result = parser.parse(expression)
            print(f"Результат: {result}")

        except CalculatorError as error:
            print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
