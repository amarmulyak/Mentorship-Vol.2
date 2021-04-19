# ***** Get dict of even numbers and their squares *****
#       7 -> {0:0, 2:4, 4:16, 6:36}

# Implementation with for loop
even_squares = dict()

for i in range(7):
    if i % 2 == 0:
        even_squares[i] = i ** 2

print(even_squares)


# Implementation with dict comprehension

even_squares_compr = {i: i ** 2 for i in range(7) if i % 2 == 0}
print(even_squares_compr)
