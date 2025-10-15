import re
from calculator_error import CalculatorError

TOKEN_RE = re.compile(r"""
\s*?
(
    [$~]?\d+(?:\.\d*)?(?:[eE][+-]?\d+)? #само число с учетом плавающей точки и унарного плюса/минуса
    |\*\*                               #возведение в степень
    |//                                 #деление нацело
    |[%()+\-*/]                         #различные операции
)
""", re.VERBOSE)


def tokenize(data: str):
    """
    Принимаем строку с математическим выражением
    возвращаем токены
    """
    if not data or not data.strip():
        raise CalculatorError("Пустой ввод")

    position = 0
    out: list[tuple] = []

    while position < len(data):
        match = TOKEN_RE.match(data, position)
        if not match:
            raise CalculatorError(f"Некорректный ввод около: '{data[position:]}'")

        token = match.group(1)
        position = match.end()

        if token[0].isdigit() or token[0] in "$~" and len(token) > 1 and token[1].isdigit():

            if token[0] == "~":
                token = "-" + token[1:]
            elif token[0] == "$":
                token = token[1:]

            try:
                out.append(("NUM", float(token)))
            except ValueError:
                raise CalculatorError(f"Некорректное число: '{token}'")
        else:
            out.append((token, None))

    out.append(("END", None))
    return out
