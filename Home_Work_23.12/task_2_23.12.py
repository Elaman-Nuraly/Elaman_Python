def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

number = int(input("Введите число для проверки: "))

result = is_power_of_two(number)
print(result)
