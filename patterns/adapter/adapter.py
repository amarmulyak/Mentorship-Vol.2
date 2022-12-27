'''
Adapter Design Pattern
'''

from abc import ABCMeta, abstractmethod

class IA(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method_a():
        'An abstract method A'
