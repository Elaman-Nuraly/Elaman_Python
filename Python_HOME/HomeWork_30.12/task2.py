"""
task 2
"""
def SelectionSort(A):

    n = len(A)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if A[j] > A[max_index]:
                max_index = j
        A[i], A[max_index] = A[max_index], A[i]

if __name__ == "__main__":
    while True:
        try:
            input_list = [1, 4, 2, 3, 4]
            SelectionSort(input_list)

            print(input_list)
            break
        except ValueError:
            print("Ошибка ввода. Введите целые числа.")
            