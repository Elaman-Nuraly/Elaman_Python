def plus_two(number):
    try:
        result = 2 + number
        print("Результат сложения: ", result)
    except TypeError:
        print("Ожидаемый тип данных — число!")

if __name__ == "__main__":
    # Запрос ввода данных у пользователя
    user_input = input("Введите число: ")

    # Попытка преобразовать введенное значение в число
    try:
        number = float(user_input)
        # Вызов функции plus_two с введенным числом
        plus_two(number)
    except ValueError:
        print("Ошибка: Введенное значение не является числом")
