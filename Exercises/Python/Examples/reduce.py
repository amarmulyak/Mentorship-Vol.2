import functools

lis = [1, 1, 2, 3, 4, 5]


def predicate_func(a, b):
    return a + b


print(functools.reduce(predicate_func, lis))


lis = [5, 3, 5, 6, 2]

print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))
print(functools.reduce(predicate_func, lis))

# Find max value in the list
print(functools.reduce(lambda a, b: a if a > b else b, lis))

