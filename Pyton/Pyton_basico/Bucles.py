my_condicion=1

while my_condicion <= 10:
    print(my_condicion)
    my_condicion += 1
else:
    print("termino el bucle")

my_list=[10, 20, 30, 40, 50]

for element in my_list:
    print(element)

numer=1
sum=0
while numer <= 100:
    sum += numer
    numer +=1
    print(sum)

word= "Python"
for letter in word:
    print(letter)

number=1
while number <= 50:
    if number %7 == 0:
        print(number)
        break
    number += 1
        
dicc = {"name":"Brais","age":37,"country":"Galicia","uwu":"onichan"}
for key in dicc:
    print(dicc)


number=1
while number <=20:
    if number%2==0:
        print(number)
    number += 1
    
for i in range(10, 0, -2):
    print(i)

list = [30, 10, 30, 20, 30, 40]
counter = 0
for number in list:
    if number == 30:
        counter += 1
print(counter)

list = [30, 10, 30, 20, 30, 40]
print(list.count(30))

names = ["Sara", "Brais", "Pedro"]
for element in names:
    if element == "Brais":
        print("se encontro Brais")
        break
    print(element)

for i in range(3):
    print(i)
