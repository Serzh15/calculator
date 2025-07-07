def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b

def power(a, b):
    if not(isinstance(a,(int, float)) and isinstance(b,(int, float))):
        raise TypeError("Arguments have to be numbers")
    return a ** b
