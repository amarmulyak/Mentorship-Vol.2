import time
import functools
import random


# Defining a decorator
def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)

    return wrap


# Applying decorator to a function
@trace
def add_two(x):
    return x + 2


# Calling the decorated function
print(add_two(3))

print("*" * 25)
# Applying decorator to a lambda
print((trace(lambda x: x ** 2))(3))

print("*" * 25)


# Decorator example
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value

    return wrapper_decorator


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


# print(return_greeting("Andriy"))


def measure_time_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        finish_time = time.perf_counter()
        duration = finish_time - start_time
        print(f"Finished {func.__name__!r} in {duration:.4f} secs")
        return value

    return wrapper


@measure_time_execution
def print_hello(num_times):
    for _ in range(num_times):
        sum([i ** 2 for i in range(10000)])


# print_hello(1)


user = {"name": "Andriy", "role": "admin"}


def make_secure(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if user["role"] == "admin":
            return func(*args, **kwargs)

    return wrapper


@make_secure
def get_user_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "5678"


# print(get_user_password("billing"))


user = {"name": "Andriy", "role": "billing"}


def factory(role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if user["role"] == role:
                return func(*args, **kwargs)

        return wrapper

    return decorator


@factory("admin")
def get_user_password():
    return "admin: 1234"


@factory("billing")
def get_dashboard_password():
    return "user: user_password"


print(get_user_password())
print(get_dashboard_password())


def debug(func):
    """Print the function signature and return value"""

    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]  # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)  # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")  # 4
        return value

    return wrapper_debug


@debug
def some_func(a, b=2, c=4):
    return a + (b * c)


print(some_func(5, b=4, c=10))

print("-" * 20)


def slow_down(func):
    """Sleep 1 second before calling the function"""

    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)

    return wrapper_slow_down


@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)


# countdown(1)

print("-" * 20)


PLUGINS = dict()


def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name):
    return f"Hello {name}"


@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)


print(randomly_greet("Andriy"))
