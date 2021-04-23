# Create generators for square and inverse
# One to return squares
# One to return 1/x (round to 2 decimals)

# Expression implementation
def square_generator(number):
    return (x ** 2 for x in range(1, number + 1))


def inverse_generator(number):
    return (round(1 / x, 2) for x in range(1, number + 1))


# squares = square_generator(5)
# print(list(squares))
# inverse = inverse_generator(5)
# print(list(inverse))


# Yield implementation
def square_generator_yield(number):
    for x in range(1, number + 1):
        yield x ** 2


squares_yield = square_generator_yield(5)
# print(list(squares_yield))


def inverse_generator_yield(number):
    for x in range(1, number + 1):
        yield round(1 / x, 2)


# inverse_yield = inverse_generator_yield(5)
# print(list(inverse_generator_yield(5)))
