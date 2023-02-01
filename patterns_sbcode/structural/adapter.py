"""
Adapter Design Pattern
"""

from abc import ABCMeta, abstractmethod

class IA(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method_a():
        """An abstract method A"""


class ClassA(IA):
    def method_a(self):
        print('Method A')


class IB(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method_b():
        """An abstract method B"""


class ClassB(IB):
    def method_b(self):
        print('Method B')


# item = ClassB()
# item.method_a()  # ClassB doesn't have method_a, that's why we need adapter


class ClassBAdapter(IA):
    def __init__(self):
        self.class_b = ClassB()

    def method_a(self):
        """Calls Method B of the Class B"""

        self.class_b.method_b()


item = ClassBAdapter()
item.method_a()
