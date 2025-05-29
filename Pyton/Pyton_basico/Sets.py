my_sets = set()
my_oyher_set = {}

print(type(my_sets))
print(type(my_oyher_set))

my_oyher_set = {"brais", "mouren", 35}
print(type(my_oyher_set))

print(len(my_oyher_set))

#un set no es una estructura ordenada
#un set no admite repetidos 

uwu = {1, 2, 3, 4, 5}
print(type(uwu))
print(uwu)

uwu.add(6)
print(uwu)

uwu.add(5)
print(uwu) #lo ignora por que ne un set no se pueden repetidos

print(3 in uwu)

uwu.remove(4)
print(uwu)

uwu.clear()
print(len(uwu))

set = {"manzana","naranja","platano"}
my_list = list(set)
print(my_list[0])

set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.union(set2))

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.difference(set2))



