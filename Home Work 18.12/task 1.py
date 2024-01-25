def count_odd_even(numbers):
    odd_count = sum(1 for num in numbers if num % 2 != 0)
    even_count = sum(1 for num in numbers if num % 2 == 0)
    return odd_count, even_count
def main():
    N = int(input("Введите длину списка: "))

    numbers = []
    even_numbers = []
    odd_numbers = []

    for i in range(N):
        num = int(input(f"Введите число {i + 1}: "))
        numbers.append(num)
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    odd_count, even_count = count_odd_even(numbers)
    print("Четные числа:")
    print(" ".join(map(str, even_numbers)))
    print("Нечетные числа:")
    print(" ".join(map(str, odd_numbers)))
    if odd_count > even_count:
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    main()
