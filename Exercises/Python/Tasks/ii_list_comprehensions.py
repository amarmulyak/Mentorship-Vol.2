"""
Get list with items divided by 3 but not divided by 6

10 -> [0, 3, 9]
Do the same using filter()
"""

# ***** Get list with items divided by 3 but not divided by 6 using List Comprehension *****
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
def filter_comprehension(func, iterable):
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
def map_comprehension(func, iterable):
    return [func(x) for x in iterable]


res = map_comprehension(lambda x: x % 3 == 0 and x / 6 != 1, range(0, 11))
# print(res)

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
def enumerate_comprehension(collection, start=0):
    return [(collection.index(x) + start, x) for x in collection]


enumerate_func_res = enumerate_comprehension(grocery, 15)
print(enumerate_func_res)
