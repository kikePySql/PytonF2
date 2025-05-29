my_tuple= tuple()
my_other_tuple=()

#las tuplas son inmutables, una vez creada no se puede modificar

my_tuple = (10, 20, 30, 40, 50)
print(my_tuple)
print(type(my_tuple))

my_other_tuple = (100, 200, 300, 400, 500)
uwu = my_other_tuple[1]
print(uwu)

my_tuple = (1, 2, 3)
my_tuple[1] = 10
print(my_tuple)

my_other_tuple = (1, 2, 3, 3, 4, 5, 3)
uwu = my_other_tuple.count(1)
print(uwu)

tupla = ("Java", "Python", "JavaScript", "Python")
uwu = tupla.index("Python")
print(uwu)

tupla = (1, 2, 3)
tupla2 = (4, 5, 6)
uwu = tupla + tupla2
print(uwu)

tupla = (10, 20, 30, 40, 50)
uwu = tupla[1:4]
print(uwu)
print(type(uwu))

tupla = ("Rojo", "Verde", "Azul")
uwu = list(tupla)
uwu.insert(1,"Amarillo")
uwu2= tuple(uwu)
print(uwu2)
print(type(uwu2))

tupla = (1, 2, 3, 5, 4)
del tupla
print(tupla)

tupla = (100, )
print(type(tupla))
print(tupla)