from copy import copy, deepcopy


class A:
    def __init__(self):
        print('init')
        self.v = 10
        self.z = [2, 3, 4]

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memo):
        print('__deepcopy__(%s)' % str(memo))
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result


# a = A()
# a.v = 11
# b1, b2 = copy(a), deepcopy(a)
# a.v = 12
# a.z.append(5)
# print(b1.v, b1.z)
# print(b2.v, b2.z)


class MyClass:
    def __init__(self, name):
        self.name = name

    def __copy__(self):
        print('__copy__()')
        return MyClass(self.name)

    def __deepcopy__(self, memo):
        print('__deepcopy__(%s)' % str(memo))
        return MyClass(deepcopy(self.name, memo))


a = MyClass('a')

sc = copy(a)
dc = deepcopy(a)
