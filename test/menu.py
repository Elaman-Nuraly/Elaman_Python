# menu.py

def show_menu():
    print("Меню калькулятора:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("q. Выход")

def get_user_choice():
    while True:
        choice = input("Введите свое значение: ")
        if choice.lower() in ['+', '-', '*', '/']:
            return choice
        elif choice.lower() == 'q':
            return 'q'
        else:
            print("Недопустимый выбор. Пожалуйста, введите допустимый оператор (+, -, *, /) или q для выхода.")
