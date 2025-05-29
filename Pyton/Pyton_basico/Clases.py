class Person:
    def __init__(self, name, surname, alias="sin alias"):
        self.full_name = f"{name} {surname} {alias}"

    def walk(self):
        print(f"{self.full_name} esta caminado") 


my_person= Person("Enrique","Almanza")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Enrique","Almanza","kikeflow")
print(my_other_person.full_name)

class Animal:
    def __init__(self, species):
        self.species = species
        
    def make_sound(self):
        if self.species == "dog":
            print("Guau")
        elif self.species == "cat":
            print("Miau")
        else:
            print("Sonido animal generico")

dog = Animal("dog")
cat = Animal("cat")
dog.make_sound()
cat.make_sound()

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._speed = 0

    def accelerate(self):
       self.__speed += 10

    def brake(self):
        self.__speed = max(0, self.__speed - 10)

mercedes = Car("mercedes benz","2025")
print(mercedes.brake)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author

    def get_author(self):
        return self.__author
    
    def change_title(self, new_title):
        self.title = new_title

libro= Book("cien años de soledad", "Gabriel garcia marquez")
libro.get_author

class Estudiante:
    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)
    
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Saldo insuficiente")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, other_pointx, other_pointy):
        distance_x = abs(self.x - other_pointx)
        distance_y = abs(self.y - other_pointy)
        return (distance_x**2 + distance_y**2)**0.5
    
z=Point(0,0)
uwu= z.calculate_distance(3,4)
print(uwu)

class Employee:
    def __init__(self, name, hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
    
    def pago_total(self):
        return (self.hourly_wage*self.hours_worked)
    
x=Employee("Enrique", 1000, 8)
nya=x.pago_total()
print(nya)

class Store: 
    def __init__(self):
        self.inventory = []

    def add_producto(self, product):
        self.inventory.append(product)

    def show_inventory(self):
        for product in self.inventory:
            print(product)

        
        
        
    
        
        


