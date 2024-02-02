# main.py
from calculator import Calculator
from menu import show_menu, get_user_choice
from operations import perform_operation
from result import show_result

def main():
    calculator = Calculator()
    while True:
        show_menu()
        choice = get_user_choice()
        if choice == 'q':
            break
        try:
            num1 = float(input("Введите Первое число: "))
            num2 = float(input("Введите Второе число: "))
        except ValueError:
            print("Ошибка: Пожалуйста, введите допустимые числовые значения.")
            continue
        if ' ' in str(num1) or ' ' in str(num2):
            print("Ошибка: Пожалуйста, введите число без пробелов.")
            continue
        result = perform_operation(choice, num1, num2, calculator)
        show_result(result)

if __name__ == "__main__":
    main()
