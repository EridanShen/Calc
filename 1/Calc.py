def calculate(expression):
    try:
        # Удаляем лишние пробелы
        expression = expression.strip()

        # Определяем оператор и разделяем строку
        if '+' in expression:
            operator = '+'
        elif '-' in expression:
            operator = '-'
        elif '*' in expression:
            operator = '*'
        elif '/' in expression:
            operator = '/'
        else:
            raise ValueError("Неверный оператор. Допустимые операторы: +, -, *, /")

        # Разделяем операнды
        operands = expression.split(operator)
        if len(operands) != 2:
            raise ValueError("Введены некорректные данные. Ожидалось два операнда и один оператор.")

        # Преобразуем операнды в целые числа
        a = int(operands[0].strip())
        b = int(operands[1].strip())

        # Проверяем, что числа находятся в пределах от 1 до 10
        if not (1 <= a <= 10 and 1 <= b <= 10):
            raise ValueError("Числа должны быть в диапазоне от 1 до 10 включительно.")

        # Выполняем арифметическую операцию и формируем строку результата
        if operator == '+':
            result = a + b
            operation = f"{result}"
        elif operator == '-':
            result = a - b
            operation = f"{result}"
        elif operator == '*':
            result = a * b
            operation = f"{result}"
        elif operator == '/':
            result = a // b  # Целочисленное деление
            operation = f"{result}"

        return operation

    except ValueError as e:
        return str(e)


# Пример использования
if __name__ == "__main__":
    user_input = input("Введите выражение (например, 3 + 5): ")
    result = calculate(user_input)
    print("Результат:", result)


