lis = [0, 2, 4, 5]


def filter_func(a):
    return a.startswith("J")


l_filter = list(filter(lambda a: a % 2 == 0, lis))
print(l_filter)


numbers = [1, 2, 3]
print(list(filter(lambda x: (x + 1) * 3 / 3 % 3 == 0, numbers)))


lis = ["Sun", "Moon", "Sea"]
print(list(filter(filter_func, lis)))
