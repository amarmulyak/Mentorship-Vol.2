(lambda x, y: x + y)(2, 5)


full_name = lambda first, last: f"Full name: {first.title()} {last.title()}"
full_name("guido", "van rossum")


(lambda x: x + 1)(2)


(lambda x, y: x + y)(2, 3)


high_ord_func = lambda x, func: x + func(x)
high_ord_func(2, lambda x: x * x)
high_ord_func(2, lambda x: x + 3)
