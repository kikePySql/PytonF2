def personalized_greeting(name = "desconocido"):
    print(f"hola {name}")

personalized_greeting()

def multiply(number1, number2):
    print(number1 * number2)

multiply(5,6)

def is_even(number1):
    if number1%2==0:
        print("es par")
    else:
        print("es impar")

is_even(9)

def convert_to_uppercase(text):
    print(text.upper())

convert_to_uppercase("nya")

def arbitrary_sum(*numbers):
    return sum(numbers)
    
def arbitrary_sum(*numbers):
    return sum(numbers)

result_sum = arbitrary_sum (5,4,3,10)
print(result_sum)

def generate_full_greeting (name, surname):
    print(f"Hola, {name} {surname}")

generate_full_greeting("Enrique","Almanza")

def power(base, exponente):
    print(base**exponente)

power(2,3)

def calculate_average(x,y,z):
    print((x+y+z)/3)

calculate_average(4,4,7)

def count_characters(texto):
    print(len(texto))

count_characters("nyanyanya")

def display_messages(*text):
    for element in text:
        print(element.upper())

display_messages("nya","uwu","blo","plo","wtf")