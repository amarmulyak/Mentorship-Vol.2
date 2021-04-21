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


it_sq = MyIterator(5, "square")
it_inv = MyIterator(5, "inverse")
it_wrong = MyIterator(5, "some")
print(list(it_sq))
print(list(it_inv))
print(list(it_wrong))
