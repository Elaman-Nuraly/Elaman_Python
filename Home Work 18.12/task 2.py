def create_matrix():
    matrix = []
    for _ in range(3):
        row_input = input("Введите три цифры через пробел: ")
        row = [int(num) for num in row_input.split()]
        matrix.append(row)
    return matrix
def sum_main_diagonal(matrix):
    diagonal_sum = sum(matrix[i][i] for i in range(3))
    return diagonal_sum
def main():
    my_matrix = create_matrix()
    print("Ваша матрица:")
    for row in my_matrix:
        print(row)
    diagonal_sum = sum_main_diagonal(my_matrix)
    print(f"Сумма элементов главной диагонали: {diagonal_sum}")
if __name__ == "__main__":
    main()
