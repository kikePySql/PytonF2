my_condition= False

if my_condition:
    print("se ejecuta la condicion del if")

my_condition= 5*5

if my_condition== 10:
    print("se ejecuta la condicion del segundo is")

if my_condition > 10 and my_condition < 20:
    print("es mayor que 10 y menor que 20")
elif my_condition==1:
    print("Es igual a 25")
else:
    print("es menor o igual que 10 o mayor o igual que 20")

print("la ejecucion continua")


numer = int(input("Ingrese un numero "))

if numer > 0:
    print("Es positivo")
elif numer==0:
    print("es 0")
else:
    print("Es negativo")


numer = int(input("Ingrese su edad "))

if numer >= 18:
    print("Es mayor de edad")

else:
    print("Es menor de edad")


strings = input("Ingrese su un texto ")

if not strings:
    print("no texto")

else:
    print("tiene texto")


numer_1 = int(input("Ingrese su numero 1: "))
numer_2 = int(input("Ingrese su numero 2: "))

if numer_1 > numer_2:
    print("1>2")
elif numer_1==numer_2:
    print("1=2")
else:
    print("1<2")

numer = int(input("Ingrese un numero "))

if numer%3==0 and numer%5==0:
    print("si es divisible por 5 y 3")

else:
    print("no es divisible")


numer = int(input("Ingrese un numero "))

if numer%2==0:
    print("es par")

else:
    print("es impar")
    
numer = int(input("Ingrese su edad "))

if numer >= 18:
    print("puede votar normal")

elif numer==16 or numer==17:
    print("Puede votarl con permiso especial")

else:
    print("Es menor de edad no vota")

strings = input("Ingrese su contraseña ")

if strings=="uwukike":
    print("correcto")

else:
    print("contraseña incorrecta")

numer = int(input("Ingrese un numero "))

if numer >= 10 and numer <=20:
    print("si")
else:
    print("no")


strings = input("Ingrese un color ").lower()

if strings=="verde":
    print("avanza")
elif strings=="amarillo":
    print("estar alerta")
elif strings=="rojo":
    print("Detente")
else:
    print("color no valido")

