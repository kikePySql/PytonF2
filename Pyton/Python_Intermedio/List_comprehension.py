numbers = [i for i in range(11)]
print(numbers)

numbers = [i**2 for i in range(1,11)]
print(numbers)

even = [i for i in range(21) if i % 2 ==0]
print(even)

celsius = [0, 10, 20, 30, 40]
fahreneit = [(temp * 9/5) + 32 for temp in celsius]
print(fahreneit)

text = "Python"
characters = [character for character in text]
print(characters)

words = ["brais", "moure", "dev", "hola","python"]
large = [p for p in words if len(p)>4]
print(large)

def sum_five(n):
    return n + 5

numbers = [1, 2, 3, 4, 5]
result = [sum_five(n) for n in numbers]
print(result)

numbers = [2, 15, 9, 42, 3]
greater = [n > 10 for n in numbers]
print(greater)

numbers = [1, 2, 3, 4, 5, 6]
odds_divisible_by_3 = [n*3 for n in numbers if n % 2 !=0]
print(odds_divisible_by_3)

matrix = [[row * 3 + col + 1 for col in range(3)] for row in range(3)]
print(matrix)