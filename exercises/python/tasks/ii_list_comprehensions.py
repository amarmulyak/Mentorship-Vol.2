from typing import Callable, List

# ***** Get list with items divided by 3 but not divided by 6 using List Comprehension *****
# 10 -> [0, 3, 9]

c1 = [x for x in range(0, 20) if x % 3 == 0 and not (x // 6 > 0 and x % 6 == 0)]
# print(c1)


# Function implementation:
def dev_3_not_dev_6(number):
    return [
        x
        for x in range(0, number + 1)
        if x % 3 == 0 and not (x // 6 > 0 and x % 6 == 0)
    ]


# print(dev_3_not_dev_6(30))


# ***** Get list with items divided by 3 but not divided by 6 using filter() *****

f = filter(lambda x: x % 3 == 0 and not (x // 6 > 0 and x % 6 == 0), range(0, 11))
# print(list(f))


# Function implementation:
def dev_3_not_dev_6_filter(number):
    return list(
        filter(
            lambda x: x % 3 == 0 and not (x // 6 > 0 and x % 6 == 0),
            range(0, number + 1),
        )
    )


# print(dev_3_not_dev_6_filter(20))


# ***** Implement filter() using list comprehension *****

# filter() example
filter_mehod = filter(lambda x: x >= 5, range(3, 8))
# print(list(filter_mehod))

# List comprehension usage
filter_compr_method = [x for x in range(3, 8) if x >= 5]
# print(filter_compr_method)


# function implementation
def filter_comprehension(func: Callable, iterable: [List, range]) -> list:
    """
    Filter the list by condition from the function
    :param func: Function with condition to verify
    :param iterable: List of elements you want to check for condition
    :return: List of elements which satisfies the condition
    """
    return [x for x in iterable if func(x)]


res_f = filter_comprehension(lambda x: x >= 5, range(3, 8))
# print(res_f)


# ***** Implement map() using list comprehension *****

# map() example
map_method = map(lambda x: x % 3 == 0 and not (x // 6 > 0 and x % 6 == 0), range(0, 20))
# print(list(map_method))

# List comprehension usage
map_compr_method = [
    x % 3 == 0 and not (x // 6 > 0 and x % 6 == 0) for x in range(0, 11)
]
# print(map_compr_method)


# function implementation
def map_comprehension(func: Callable, iterable: [List, range]) -> list:
    """
    Apply function to each element in the list
    :param func: Function you want to apply
    :param iterable: List of elements you want to apply function on
    :return: List of the new elements processed by the function
    """
    return [func(x) for x in iterable]


res = map_comprehension(
    lambda x: x % 3 == 0 and not (x // 6 > 0 and x % 6 == 0), range(0, 11)
)
# print(res)


# ***** Implement enumerate() using list comprehension *****

# enumerate() example
grocery = ["bread", "milk", "butter"]
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
    :param collection: List of elements you want to enumerate
    :param start: The number from which enumeration should start, default 0
    :return: List of tuples with enumeration
    """
    return [(collection.index(x) + start, x) for x in collection]


# enumerate_func_res = enumerate_comprehension(grocery, 15)
enumerate_func_res = enumerate_comprehension(range(5), 15)
# print(enumerate_func_res)
