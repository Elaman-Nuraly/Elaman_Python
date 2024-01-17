"""
home_work_9
"""
def merge_files(file_names, output_file):
    with open(output_file, 'w', encoding='utf-8') as output:
        for file_name in file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    output.write(file.read())
                    output.write('\n')  # Добавляем разделитель между содержимым файлов
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
            except Exception as e:
                print(f"Произошла ошибка при чтении файла {file_name}: {e}")
def main():
    file_names = []
    while True:
        file_name = input("Введите название файла (или 'quit' для завершения): ")
        if file_name.lower() == 'quit':
            break
        else:
            file_names.append(file_name)
    if not file_names:
        print("Список файлов пуст. Программа завершена.")
        return
    output_file = input("Введите название файла для объединения содержимого: ")
    try:
        merge_files(file_names, output_file)
        print(f"Содержимое файлов успешно объединено в файл {output_file}.")
    except Exception as e:
        print(f"Произошла ошибка при объединении файлов: {e}")
if __name__ == "__main__":
    main()