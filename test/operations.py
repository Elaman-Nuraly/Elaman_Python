# operations.py
from calculator import Calculator

def perform_operation(operator, x, y, calculator):
    if operator == '+':
        return calculator.add(x, y)
    elif operator == '-':
        return calculator.subtract(x, y)
    elif operator == '*':
        return calculator.multiply(x, y)
    elif operator == '/':
        return calculator.divide(x, y)
    else:
        return "Invalid operator"
