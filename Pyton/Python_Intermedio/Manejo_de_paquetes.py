import math
import numpy
import pandas
import requests
from mypackage import arithmetics
print(arithmetics.sum_two_values(3, 7))

print("el valor de pi es:", math.pi)

array = numpy.array([10, 20, 30])
print(array * 3)

print("version de numpy:", numpy.version.version)

response = requests.get("https://pokeapi.co/api/v2/pokemon/squirtle")
print("codigo de estado:", response.status_code)

data = {"nombre":["Brais", "Sara"], "Edad": [37, 45]}
df = pandas.DataFrame(data)
print(df)

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=5")
data = response.json()
names = [p["name"] for p in data["results"]]
print("Nombres:", names)

#pip list (desde la terminal)
#help(numpy)