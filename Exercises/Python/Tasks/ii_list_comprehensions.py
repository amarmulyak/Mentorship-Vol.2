"""
Get list with items divided by 3 but not divided by 6

10 -> [0, 3, 9]
Do the same using filter()
"""

c1 = [x for x in range(0, 11) if x % 3 == 0 and not (x // 6 == 1 and x % 6 == 0)]
# print(c1)

c2 = [x for x in range(0, 11) if x % 3 == 0 and x / 6 != 1]
# print(c2)
