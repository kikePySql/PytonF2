my_list = list()
my_oyher_list=[]

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30,17]
print(my_list.pop())

print(len(my_list))
print(my_list)

my_oyher_list = [35, 1.77, "brais", "mouren"]

my_oyher_list.append("mouredev")
print(my_oyher_list)

my_oyher_list.insert(1, "Azul")
print(my_oyher_list)

my_oyher_list.remove("Azul")
print(my_oyher_list)

print(my_oyher_list[0])
print(my_oyher_list[1])
print(my_oyher_list[-1])
print(my_oyher_list[-3])
print(my_oyher_list[-4])
print(my_list.count(30))

print(my_list+my_oyher_list)

list = [1, 2, 3, 4, 5]
print(list)

list = [10, 20, 30, 40, 50]
print(list[2])

list = [1, 2, 3, 4, 5]
list.append(6)
print(list)

list = [10, 20, 30, 40, 50]
list.insert(1, 15)
print(list)

list = [10, 20, 30, 30, 40, 50]
list.remove(30)
print(list)

list = [1, 2, 3, 4, 5]
pop=list.pop(4)
print(pop)
print(list)

list = [100, 200, 300, 400, 500]
list.reverse()
print(list)

list=[3, 1, 4, 2, 5]
list.sort()
print(list)

list=[1, 2, 3]
list2=[4, 5, 6]
list3=list+list2
print(list3)

list = [10, 20, 30, 30, 40, 50]
my_new_list=list[1:3]
print(my_new_list)

list = [1, 2, 3, 4, 5]
print(list[1:4])
