def access_array_element(array, index):
    try:
        value = array[index]
        print("Значение элемента с индексом", index, ":", value)
    except IndexError:
        print("Ошибка: Индекс выходит за границы массива")

def main():
    my_array = [1, 2, 3, 4, 5]

    try:
        index = int(input("Введите индекс элемента массива: "))
        access_array_element(my_array, index)
    except ValueError:
        print("Ошибка: Введите целое число в качестве индекса")

if __name__ == "__main__":
    main()
