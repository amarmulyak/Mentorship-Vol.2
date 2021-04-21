# def some_func(x):
#     if x > 2:
#         return x


# print(bool(some_func(1)))


# print((lambda x: x > 5)(4))


# d = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5 }
# iterable = d.keys()
# iterator = iter(iterable)
# print( next(iterator) )
# print( next(iterator) )


# from itertools import count
#
#
# sequence = count(start=0, step=1)
#
# while(next(sequence) <= 10):
#     print(next(sequence))
# i = 0
# while i <= 10:
#     print(i)
#     i += 1
#
# com = [i for i in range(2)]

# pos_el = (pos for pos in range(2))
# print(list(pos_el))

#
# def series_generator(low, high):
#     while low <= high:
#         yield low
#         low += 1

# from datetime import datetime

# print(datetime.now().strftime("%d/%m/%y %H:%M:%S"))

import time


# def func(seconds):
#     while seconds >= 5:
#         print("Second is more then 5")
#         seconds -= 1
#
#
# func(5)
#
# i = 1/3
# print(round(i, 2))

