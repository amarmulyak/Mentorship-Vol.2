# def outer_func(x):
#     y = 4
#     def inner_func(z):
#         print(f"x = {x}, y = {y}, z = {z}")
#         return x + y + z
#     return inner_func


# for i in range(3):
#     closure = outer_func(i)
#     print(f"closure({i+5}) = {closure(i+5)}")


def wrap(n):
    def f():
        print(n)
    return f


numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(wrap(n))

for f in funcs:
    f()
