# Generator function
def series_generator(low, high):
    while low <= high:
        yield low
        low += 1


n_list = []
for num in series_generator(1, 10):
    n_list.append(num)

# print(n_list)


# Generator expression
squares = (x * x for x in range(1, 10))
print(type(squares))
print(list(squares))
