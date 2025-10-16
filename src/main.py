from src.expression_parser import calculate_expression
from src.calculator_error import CalculatorError


def main() -> None:
    """
    Основная функция работы калькулятора
    """

    while True:
        try:
            expression = input("\nВведите выражение: ").strip()

            result = calculate_expression(expression)
            print(f"Результат: {result}")

        except CalculatorError as error:
            print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
