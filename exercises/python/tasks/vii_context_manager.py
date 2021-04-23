# Context Manager
# o Create Timer context manager
#   § Prints “Timer start” at the beginning
#   § Prints “Code block took x.xxx seconds” at the end.
# o Implement the same using @contextmanager


import time


class Timer:
    def __init__(self):
        self.start_time = time.time()

    def __enter__(self):
        print("Timer start")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = round(time.time() - self.start_time, 2)
        print(f"Code block took {duration} seconds")


with Timer() as t:
    a = [x**100 for x in range(1, 1000000)]
