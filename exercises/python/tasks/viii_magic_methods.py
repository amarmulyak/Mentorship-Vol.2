import copy


class Version:
    def __init__(self, version_number):
        self.version_number = version_number
        self.parts = [int(part) for part in version_number.split(".")]

    def __repr__(self):
        return f"\nVersion {self.version_number!r}"

    def __gt__(self, other):
        pos = 0
        for _ in range(len(self.parts)):
            if self.parts[pos] > other.parts[pos]:
                return True
            pos += 1
        return False

    def __ge__(self, other):
        pos = 0
        for _ in range(len(self.parts)):
            if self.parts[pos] < other.parts[pos]:
                return False
            if self.parts[pos] > other.parts[pos]:
                return True
            pos += 1
        return True

    def __lt__(self, other):
        pos = 0
        for _ in range(len(self.parts)):
            if self.parts[pos] < other.parts[pos]:
                return True
            pos += 1
        return False

    def __le__(self, other):
        pos = 0
        for _ in range(len(self.parts)):
            if self.parts[pos] > other.parts[pos]:
                return False
            if self.parts[pos] < other.parts[pos]:
                return True
            pos += 1
        return True

    def __eq__(self, other):
        pos = 0
        for _ in range(len(self.parts)):
            if self.parts[pos] != other.parts[pos]:
                return False
            pos += 1
        return True

    def __ne__(self, other):
        pos = 0
        for _ in range(len(self.parts)):
            if self.parts[pos] != other.parts[pos]:
                return True
            pos += 1
        return False

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, copy.deepcopy(v, memo))
        return result


ver1 = Version("1.2.3.5")
# ver2 = Version("2.2.3.5")
# print(ver1, ver2)
# print("ver1 > ver2", ver1 > ver2)
# print("ver1 >= ver2", ver1 >= ver2)
# print("ver1 < ver2", ver1 < ver2)
# print("ver1 <= ver2", ver1 <= ver2)
# print("ver1 == ver2", ver1 == ver2)
# print("ver1 != ver2", ver1 != ver2)

ver3 = copy.copy(ver1)
ver4 = copy.deepcopy(ver1)
# print(ver1)
# print(ver3)
# print(ver4)

print(ver3.__dict__)
ver3.__setattr__("test", "TEST")
print(ver3.__dict__)
