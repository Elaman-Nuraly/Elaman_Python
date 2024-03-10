"""
task 4
"""
def find_closest_numbers(numbers):

    sorted_numbers = sorted(numbers)
    min_difference = float('inf')
    result_pair = None
    for i in range(len(sorted_numbers) - 1):
        current_difference = sorted_numbers[i + 1] - sorted_numbers[i]
        if current_difference < min_difference:
            min_difference = current_difference
            result_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    return result_pair

if __name__ == "__main__":

    while True:
        try:
            input_numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
            if len(input_numbers) < 2:
                raise ValueError("Список должен содержать не менее двух элементов")
            result = find_closest_numbers(input_numbers)
            
            print("Два ближайших числа:", result)
            break
        except ValueError as e:

            print(f"Ошибка ввода: {e}")
