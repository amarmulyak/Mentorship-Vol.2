def some_func(a):
    return a*2


lis = [1, 2, 3]
l_map = list(map(some_func, lis))
l_map2 = list(map(lambda x: x * 2, lis))

# print(l_map)
# print(l_map2)


"""
Next example
"""
from exercises.python.examples.decorator_examples import debug


@debug
def multiply(x):
    return x * x


@debug
def add(x):
    return x + x


funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]
