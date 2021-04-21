a_set = {1, 2, 3}
b_iterator = iter(a_set)
print(next(b_iterator))
print(type(a_set))
print(type(b_iterator))


class Series(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 2
            return self.current - 2


n_list = Series(1, 10)
# print(list(n_list))
