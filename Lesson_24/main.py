# main.py
from calculator import Calculator 
from menu import Menu

def main(): 
    calculator = Calculator() 
    menu = Menu() 
    while True: 
        menu.get_start() 
        choice = menu.get_choice() 
        print("="*20) 
        if choice == '5': 
            break 
        try: 
            num1 = float(input("Введите первое число: ")) 
            num2 = float(input("Введите второе число: ")) 
        except ValueError: 
            print("Ошибка: Пожалуйста, введите допустимые числовые значения.")  
        except ZeroDivisionError: 
                print("Ошибка: Нельзя делить на ноль!") 
                continue 
        except TypeError: 
                print("Просто ошибка!") 
                continue 
        result = perform_operation(choice, num1, num2, calculator) 
        show_result(result) 

if __name__ == "__main__": 
    main()
