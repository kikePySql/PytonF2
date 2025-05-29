import re

text = "Hola Python"
match = re.match("Hola", text)
print(match)

text = "Estoy aprendiendo python"
search = re.search("Python", text, re.I)
print(search is not None)

text = "Este curso es un curso de Python intermedio"
results = re.findall("curso", text)
print(results)

text = "Esta leccion es importante. Otra leccion vendra despues"
new_text = re.sub("leccion", "LECCION", text)
print(new_text)

text = "Ayer aprendi algo nuevo"
match = re.search(r"\b[aA]\w+",text)
print(match.group())

text = "Uno,Dos,Tres,Cuatro"
parts = re.split(",", text)
print(parts)

text = "Educacion, programacion y diversion"
results = re.findall(r"\w+cion", text)
print(results)

text = "123456"
match = re.fullmatch(r"\d+", text)
print(match is not None)

text = "Estoy aprendiendo 2 lenguajes y 3 frameworks"
new_text = re.sub(r"\d+", "[numero]", text)
print(new_text)

text = "Este dato vale oro en esta clase"
results = re.findall(r"\b\w{4}\b", text)
print(results)