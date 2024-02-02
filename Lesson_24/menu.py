# menu.py

class Menu:

    def get_start(self):
        print(
        "1. Сложение",
        "2. Вычитание",
        "3. Умножение",
        "4. Деление",
        "5. Выход", sep="\n")
        print("="*20)

    def get_choice(self):
        return input("Введите операцию:")

def perform_operation(operator, x, y, calculator):
    if operator == '1':
        return calculator.add(x, y)
    elif operator == '2':
        return calculator.subtract(x, y)
    elif operator == '3':
        return calculator.multiply(x, y)
    elif operator == '4':
        return calculator.divide(x, y)
    else:
        return "Неверный оператор"

def show_result(result):
    if result is not None:
        print("Результат:", result)
