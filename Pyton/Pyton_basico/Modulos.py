#calculator.py

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "No se puede dividir entre cero"
    return a/b

# Impotancia desde otro fichero

# from calculator import add, subtract, multiply, divide
# print(add(5, 3))
# print(subtract(5, 3))
# print(multiply(5, 3))
# print(divide(5, 3))