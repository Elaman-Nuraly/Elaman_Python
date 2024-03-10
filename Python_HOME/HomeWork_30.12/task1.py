"""
task 1
"""
def InsertionSort(A):

    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

if __name__ == "__main__":
    while True:
        try:
            input_list = [1, 4, 2, 3, 4]
            InsertionSort(input_list)

            print(input_list)

            break
        except ValueError:
            print("Ошибка ввода. Введите целые числа.")
