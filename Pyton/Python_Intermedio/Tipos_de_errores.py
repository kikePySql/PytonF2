import math
from math import pi

#Error SyntaxError
#print "hola mundo"

#Error NameError
#print(language)

#Error IndexError
#my_list = ["uno", "dos", "tres"]
#print(my_list[5])

#Error ModeleNotFoundError
#import maths

#Error AttributeError
#print(math.PI)

#Error KeyError
#my_dict = {"name":"Brais","age":37}
#print(my_dict["surname"])

#Error TypeError
#my_list = [1, 2, 3]
#print(my_list["0"])

#Error ImportError
#from math import PI

#Error ValueError
#my_int = int("10 años")

#Error
my_dict = {"course": "Python"}
try:
    print(my_dict["level"])
except KeyError:
    print("Error: clave no encontrada")
