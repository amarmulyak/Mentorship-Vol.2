from datetime import datetime
import time


#  Create decorator that prints function name, parameters, execution time.
def function_information(func):
    def wrapper(*args, **kwargs):
        print(f'Function: {func.__name__} '
              f'\nParameters: args - {args} kwargs - {kwargs}'
              f'\nExecution time: {datetime.now().strftime("%d/%m/%y %H:%M:%S")}')
        return func(*args, **kwargs)
    return wrapper


@function_information
def test_function(name, age=0):
    print("Name: {}, Age: {}".format(name, age))


# test_function("Andriy", age=12)


#  Create wait decorator that executes function for X seconds until it returns Y.
def expecting_result(seconds: int, result):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            while seconds - (time.time() - start) >= 0:
                func_result = func(*args, **kwargs)
                if func_result == result:
                    return f'Actual is equal to expected ({func_result} = {result})'
            else:
                return f"Function didn't return {result!r} result"
        return wrapper
    return decorator


@expecting_result(5, "Hello")
def func_spell(word):
    return word


# print(func_spell("Hello2"))


def decorator_singleton(class_):
    instances = dict()

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance


@decorator_singleton
class SomeClass:
    def __init__(self, par1, par2):
        self.par1 = par1
        self.par2 = par2

    def __repr__(self):
        return f"SomeClass: {self.par1}, {self.par2}"


my_class = SomeClass("Hello", "World")
my_class2 = SomeClass("Hello2", "World2")
print(my_class)
print(my_class2)
print(my_class is my_class2)
