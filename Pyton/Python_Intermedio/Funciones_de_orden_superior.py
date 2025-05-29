from functools import reduce

def apply_function(f, value):
    return f(value)

print(apply_function(lambda x: x+3,10))

def add_and_apply(a,b,f):
    return f(a+b)

print(add_and_apply(2,3, lambda x: x*2))

def make_adder(fixed):
    return lambda x: x+fixed

add_five = make_adder(5)
print(add_five(10))

numbers = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x*10, numbers))
print(result)

numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x%2 ==0, numbers))
print(even)

numbers = [1, 2, 3, 4, 5, 6]
total = reduce(lambda x, y: x+y, numbers)
print(total)

def greeting_function():
    return lambda name: "hola, "+ name

greet = greeting_function()
print(greet("Brais"))

def count_matches(lst, condition):
    count = 0
    for item in lst:
        if condition(item):
            count += 1
    return count

print(count_matches([1, 5, 8, 3], lambda x: x>4))

def apply_both(f1, f2, value):
    return f2(f1(value))

print(apply_both(lambda x: x+2, lambda x: x*3, 4))

def apply_to_list(lst, f):
    result = []
    for item in lst:
        result.append(f(item))
    return result

print(apply_to_list([1, 2, 3], lambda x: x*2))

