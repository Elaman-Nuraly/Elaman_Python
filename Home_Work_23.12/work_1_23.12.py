import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Диалог с пользователем
while True:
    print("\nВыберите операцию:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (x^y)")
    print("6. Факториал")
    print("7. Число Фибоначчи")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("11. Выход")

    choice = input("Ваш выбор: ")

    if choice == '11':
        print("Выход из программы.")
        break

    try:
        if choice in {'1', '2', '3', '4', '5'}:
            x = float(input("Введите первое число: "))
            y = float(input("Введите второе число: "))
        elif choice in {'6', '7'}:
            x = int(input("Введите число: "))
        else:
            x = float(input("Введите угол в градусах: "))
    except ValueError:
        print("Ошибка: Введите корректное число.")
        continue

    if choice == '1':
        result = x + y
    elif choice == '2':
        result = x - y
    elif choice == '3':
        result = x * y
    elif choice == '4':
        if y == 0:
            print("Ошибка: Деление на ноль.")
            continue
        result = x / y
    elif choice == '5':
        result = x ** y
    elif choice == '6':
        result = factorial(x)
    elif choice == '7':
        result = fibonacci(x)
    elif choice in {'8', '9', '10'}:
        x_rad = math.radians(x)
        if choice == '8':
            result = math.sin(x_rad)
        elif choice == '9':
            result = math.cos(x_rad)
        elif choice == '10':
            result = math.tan(x_rad)

    print(f"Результат: {result}")
