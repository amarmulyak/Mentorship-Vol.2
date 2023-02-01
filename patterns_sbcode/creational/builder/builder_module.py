'''
// Using the Builder pattern makes sense only when your products
// are quite complex and require extensive configuration. The
// following two products are related, although they don't have
// a common interface.
'''
from abc import ABCMeta

from dataclasses import dataclass


class Engine(metaclass=ABCMeta):
    '''
    Abstract Engine class
    '''


class SportEngine(Engine):
    '''
    class SportEngine
    '''

    def __init__(self):
        self.engine = 'Sport Engine'

    def __str__(self):
        return self.engine


class RegularEngine(Engine):
    '''
    class RegularEngine
    '''

    def __init__(self):
        self.engine = 'Regular Engine'

@dataclass
class Car:
    '''
    // A car can have a GPS, trip computer and some number of
    // seats. Different models of cars (sports car, SUV,
    // cabriolet) might have different features installed or
    // enabled.
    '''
    seats: int = None
    engine: Engine = None
    trip_computer: bool = None
    gps: bool = None


@dataclass
class Manual:
    '''
    // Each car should have a user manual that corresponds to
    // the car's configuration and describes all its features.
    '''
    seats: str = None
    engine: str = None
    trip_computer: str = None
    gps: str = None
