"""
o Create iterable with two iterators (starts from 1):
    § One to return squares
    § One to return 1/x (round to 2 decimals)
    § X(n, type_)
    § X(5, “square”) -> 1, 4, 9, 16, 25
    § X(5, “inverse”) -> 1, 0.5, 0.33, 0.25, 0.2
"""


class MyIterator:
    def __init__(self, number, action):
        self.number = number
        self.current = 1
        self.action = action
        if action not in ["square", "inverse"]:
            raise ValueError("Action should be 'square' or 'inverse'")

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.number:
            raise StopIteration
        elif self.action == "square":
            self.current += 1  # I don't like this dupe code
            return (self.current - 1) ** 2
        elif self.action == "inverse":
            self.current += 1  # I don't like this dupe code
            return round(1 / (self.current - 1), 2)
        else:
            self.current += 1
            return self.current - 1


# it_sq = MyIterator(5, "square")
# it_inv = MyIterator(5, "inverse")
# it_wrong = MyIterator(5, "some")
# print(list(it_sq))
# print(list(it_inv))
# print(list(it_wrong))


# Method 2
class SquareIterator:
    def __init__(self, number):
        self.number = number
        self.current = 1

    def __next__(self):
        if self.current > self.number:
            raise StopIteration
        else:
            self.current += 1
            return (self.current - 1) ** 2


class InverseIterator:
    def __init__(self, number):
        self.number = number
        self.current = 1

    def __next__(self):
        if self.current > self.number:
            raise StopIteration
        else:
            self.current += 1
            return round(1 / (self.current - 1), 2)


# Created instances
class MyIterable1:
    def __init__(self, number, type_):
        self.square = SquareIterator(number)
        self.inverse = InverseIterator(number)
        self.type_ = type_

    def __iter__(self):
        if self.type_ == "square":
            return self.square
        else:
            return self.inverse


# Called classes
class MyIterable2:
    def __init__(self, number, type_):
        self.number = number
        self.type_ = type_
        if type_ not in ["square", "inverse"]:
            raise ValueError("Type should be 'square' or 'inverse'")

    def __iter__(self):
        if self.type_ == "square":
            return SquareIterator(self.number)
        elif self.type_ == "inverse":
            return InverseIterator(self.number)


sq = MyIterable2(10, "square")
inv = MyIterable2(7, "inverse")

print(list(sq))
print(list(inv))
