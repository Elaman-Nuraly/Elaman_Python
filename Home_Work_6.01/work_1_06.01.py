"""
home work 1
"""
def task_1(input_list):
    return {x: x**3 for x in input_list if x % 2 != 0}
def task_2(input_list):
    return {x for x in input_list if x % 2 == 0}
def task_3(input_list):
    return [x * 10 for x in range(len(input_list))]
def divisible_by_7_generator(n):
    current = 0
    while current <= n:
        if current % 7 == 0:
            yield current
        current += 1
if __name__ == "__main__":
    while True:
        try:
            input_list = input("Введите список: ").split()
            input_list = list(map(int, input_list))
            result_1 = task_1(input_list)
            result_2 = task_2(input_list)
            result_3 = task_3(input_list)
            n = int(input("Введите верхнюю границу делящихся на 7 чисел: "))
            generator_result = list(divisible_by_7_generator(n))
            print("Результат задачи 1:", result_1)
            print("Результат задачи 2:", result_2)
            print("Результат задачи 3:", result_3)
            print("Результат задачи 4:", generator_result)
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")