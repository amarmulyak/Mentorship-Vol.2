'''
// The builder interface specifies methods for creating the
// different parts of the product objects.
'''

from abc import ABCMeta, abstractmethod

from patterns.creational.builder.builder import Car


class Builder(metaclass=ABCMeta):
    '''
    Docsting
    '''

    @abstractmethod
    def reset(self):
        '''
        Docsting
        '''

    @abstractmethod
    def set_seats(self):
        '''
        Docsting
        '''

    @abstractmethod
    def set_engine(self):
        '''
        Docsting
        '''

    @abstractmethod
    def set_trip_computer(self):
        '''
        Docsting
        '''

    @abstractmethod
    def set_gps(self):
        '''
        Docsting
        '''


class CarBuilder(Builder):
    '''
    // The concrete builder classes follow the builder interface and
    // provide specific implementations of the building steps. Your
    // program may have several variations of builders, each
    // implemented differently.
    '''

    def __init__(self, car: Car):
        self._car = car


    @classmethod
    def reset(cls):
        '''
        // The reset method clears the object being built.
        '''

        cls.car = Car()
