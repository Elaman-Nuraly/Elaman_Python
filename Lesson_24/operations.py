# operations.py
from calculator import Calculator

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
