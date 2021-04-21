from typing import Callable

# ***** Get list with items divided by 3 but not divided by 6 using List Comprehension *****
# 10 -> [0, 3, 9]

c1 = [x for x in range(0, 11) if x % 3 == 0 and not (x // 6 == 1 and x % 6 == 0)]
# print(c1)

# method 2
c2 = [x for x in range(0, 11) if x % 3 == 0 and x / 6 != 1]
# print(c2)


# ***** Get list with items divided by 3 but not divided by 6 using filter() *****

f = filter(lambda x: x % 3 == 0 and x / 6 != 1, range(0, 11))
# print(list(f))


# ***** Implement filter() using list comprehension *****

# filter() example
filter_mehod = filter(lambda x: x >= 5, range(3, 8))
# print(list(filter_mehod))

# List comprehension usage
filter_compr_method = [x for x in range(3, 8) if x >= 5]
# print(filter_compr_method)


# function implementation
def filter_comprehension(func: Callable, iterable: [list, range]) -> list:
    """
    Filters the list by condition from the function
    :param func: function with condition to verify
    :param iterable: list of elements you want to check for condition
    :return: list of elements which satisfies the condition
    """
    return [x for x in iterable if func(x)]


res_f = filter_comprehension(lambda x: x >= 5, range(3, 8))
# print(res_f)

# ***** Implement map() using list comprehension *****

# map() example
map_method = map(lambda x: x % 3 == 0 and x / 6 != 1, range(0, 11))
# print(list(map_method))

# List comprehension usage
map_compr_method = [x % 3 == 0 and x / 6 != 1 for x in range(0, 11)]
# print(map_compr_method)


# function implementation
def map_comprehension(func: Callable, iterable: [list, range]) -> list:
    """
    Applies function to each element in the list
    :param func: function you want to apply
    :param iterable: list of elements you want to apply function on
    :return: list of the new elements processed by the function
    """
    return [func(x) for x in iterable]


res = map_comprehension(lambda x: x % 3 == 0 and x / 6 != 1, range(0, 11))
# print(res)

# print(type(map_comprehension))

# ***** Implement enumerate() using list comprehension *****

# enumerate() example
grocery = ['bread', 'milk', 'butter']
enumerate_res = enumerate(grocery)
# print(list(enumerate_res))


# Implementation with for loop
enumerate_for_res = []
pos = 0
for val in grocery:
    enumerate_for_res.append((pos, val))
    pos += 1

# List comprehension usage
enumerate_compr_res = [(grocery.index(val), val) for val in grocery]
# print(enumerate_compr_res)


# function implementation
def enumerate_comprehension(collection: [range, list], start: int = 0) -> list:
    """
    Enumerate list of elements
    :param collection: list of elements you want to enumerate
    :param start: the number from which enumeration should start, default 0
    :return: list of tuples with enumeration
    """
    return [(collection.index(x) + start, x) for x in collection]


# enumerate_func_res = enumerate_comprehension(grocery, 15)
enumerate_func_res = enumerate_comprehension(range(5), 15)
print(enumerate_func_res)
