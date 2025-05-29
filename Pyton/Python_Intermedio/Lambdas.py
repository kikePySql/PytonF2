sum_two_values=lambda first_value,second_value: first_value + second_value
print(sum_two_values(2, 4))

sum = lambda a,b: a+b
print(sum(3,5))

square = lambda x: x**2
print(square(6))

greater = lambda a,b: a if a > b else b
print(greater(10,25))

add_ten = lambda x: x+10
print(add_ten(7))

last_char = lambda text: text[-1]
print(last_char("python"))

long_word = lambda word: len(word)>6
print(long_word("Python"))
print(long_word("moureDev"))

is_positive = lambda number: number>0
print(is_positive(-1))
print(is_positive(8))

check_empty = lambda s: "cadena vacia" if s== "" else "cadena no vacia"
print(check_empty(""))
print(check_empty("python"))

price_with_tax = lambda price: price*1.21
print(price_with_tax(100))



