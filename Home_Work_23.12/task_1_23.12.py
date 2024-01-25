def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def get_fibonacci_sequence(numbers):
    sequence = [fibonacci(number) for number in numbers]
    return sequence
# Получение от пользователя чисел Фибоначчи
try:
    user_input = input("Введите числа Фибоначчи через пробел: ")
    numbers = [int(num) for num in user_input.split()]
    if any(num < 0 for num in numbers):
        raise ValueError("Введите положительные числа.")
except ValueError as e:
    print(f"Ошибка: {e}")
else:
    # Получение последовательности чисел Фибоначчи
    fibonacci_sequence = get_fibonacci_sequence(numbers)
    # Вывод результатов
    print(f"Числа Фибоначчи: {fibonacci_sequence}")
