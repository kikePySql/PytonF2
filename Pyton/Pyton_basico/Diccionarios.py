my_dict = {"Name":"Enrique", "Age":27, "Country":"Medellin"}
print(my_dict)
print(type(my_dict))
print(my_dict.items())

print(my_dict["Name"])
my_dict["Job"]="Programador"
print(my_dict)

my_dict["Age"]=38
print(my_dict)

del my_dict["Country"]
print(my_dict)

number_dict={1:1, 2:4, 3:9, 4:16, 5:25}

dic = {"Name":"Brais","Age":37,"country":"Galicia"}

other_dic=dic.fromkeys("job")
print(other_dic)

my_keys = ["name", "age", "job"]
my_new_dict = dict.fromkeys(my_keys, "Desconocido")
print(my_new_dict)