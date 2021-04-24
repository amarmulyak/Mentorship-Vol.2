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


ver1 = Version("1.2.3.5")
ver2 = Version("2.2.3.5")
print(ver1, ver2)
print("ver1 > ver2", ver1 > ver2)
print("ver1 >= ver2", ver1 >= ver2)
print("ver1 < ver2", ver1 < ver2)
print("ver1 <= ver2", ver1 <= ver2)
print("ver1 == ver2", ver1 == ver2)
print("ver1 != ver2", ver1 != ver2)
