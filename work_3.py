"""
home_work_3
"""
import re
def split_string(input_string, separators):
    separators_pattern = '|'.join(map(re.escape, separators))
    parts = re.split(separators_pattern, input_string)
    return [part.strip() for part in parts if part.strip()]
if __name__ == "__main__":
    while True:
        try:
            input_string = input("Введите строку: ")
            input_separators = input("Введите разделители: ").split()
            result = split_string(input_string, input_separators)
            if result:
                print("Результат разбиения строки:", result)
            else:
                print("Строка не содержит значимых частей.")
                break
        except Exception as e:
            print(f"Произошла ошибка: {e}")