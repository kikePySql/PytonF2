def divide_numbers(num1, num2):
    try:
        result = num1/num2
        print(f"el resultado es {result}")
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")
    
divide_numbers(9,1)

def convert_to_integer(string):
    try:
        return int(string)
    except ValueError:
        print("Error: no se puede transformar a entero")

convert_to_integer("uwu")

def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: fichero no encontrado")

read_file()

def perform_operations(num1,num2):
    try:
        print(f"suma: {num1+num2}")
        print(f"resta: {num1-num2}")
        print(f"multiplicacion: {num1*num2}")
        print(f"divicion: {num1/num2}")
    except ZeroDivisionError:
        print("Error: no se puede divider entre 0")
    else:
        print("Operaciones realizadas correctamente")
    finally:
        print("fin de las operaciones")

perform_operations(5,0)

def ask_age():
    try:
        age = int(input("Introduce tu edad: "))
        if age<=0:
            raise ValueError("La edad dede ser un entero positivo")
        return age
    except ValueError as e:
        print(f"Error: {e}")

ask_age()

def handle_multiple_exceptions(num1,num2):
    try:
        result = num1/num2
        print(f"result: {result}")
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero")
    except ValueError:
        print("Error: Valor invalido")
    except TypeError:
        print("Error: tipo no compatible")
    
handle_multiple_exceptions(3,0)

class InsufficientFundsError(Exception):
    pass

def simulate_transaction(balance, withdrawal_amount):
    try:
        if withdrawal_amount > balance:
            raise InsufficientFundsError("saldo insuficiente para la transaccion.")
        balance -= withdrawal_amount
        print(f"Transaccion realizada correctamente. Nuevo saldo: {balance}")
    except InsufficientFundsError as e:
        print(f"Error: {e}")

simulate_transaction(1000, 1100)

def convert_list_to_integers(string_list):
    integers = []
    for string in string_list:
        try:
            integers.append(int(string))
        except ValueError:
            print(f"Error: {string} no se puede transformar en un entero.")
    return integers

convert_list_to_integers()

def calculate_square_root(number):
    try:
        if number < 0:
            raise ValueError("No se puede calcular la raiz cuadrada de un numero negativo.")
        return number**0.5
    except ValueError as e:
        print(f"Error: {e}")

calculate_square_root(-89)
            

