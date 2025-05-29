import os

file = open("example.txt", "w")
file.write("hola desde python")
file.close()

#os.remove("example.txt")

file = open("example.txt", "r")
print(file.read())
file.close()

file = open("example.txt", "a")
file.write("\nLinea Añadida")
file.close()

file = open("example.txt", "r")
print(file.read(10))
file.close()

file = open("example.txt", "r")
file.seek(0)
print(file.read())
file.close()

file = open("example.txt", "r")
print(file.readline())
print(file.readline())
file.close

file = open("example.txt", "r")
lines = file.readlines()
for line in lines:
    print(line.strip())
file.close()

file = open("new_file.txt","w")
file.write("primera linea\nsegunda linea\nTercera linea")
file.close()

with open("with_file.txt", "w") as file:
    file.write("Este archivo se maneja con with")

with open("example.txt", "r") as file:
    for line in file:
        if "python" in line:
            print(line.strip())