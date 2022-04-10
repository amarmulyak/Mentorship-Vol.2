'''
// The builder interface specifies methods for creating the
// different parts of the product objects.
'''

from abc import ABCMeta, abstractmethod

from patterns.creational.builder.builder_module import Car, Manual, Engine


class Builder(metaclass=ABCMeta):
    '''
    Abstract Builder class
    '''

    @abstractmethod
    def reset(self):
        '''
        Abstract reset method
        '''

    @abstractmethod
    def set_seats(self, number_of_seats: int):
        '''
        Abstract reset method
        '''

    @abstractmethod
    def set_engine(self, engine: Engine):
        '''
        Abstract reset method
        '''

    @abstractmethod
    def set_trip_computer(self, trip_computer: bool):
        '''
        Abstract reset method
        '''

    @abstractmethod
    def set_gps(self, gps: bool):
        '''
        Abstract reset method
        '''


class CarBuilder(Builder):
    '''
    // The concrete builder classes follow the builder interface and
    // provide specific implementations of the building steps. Your
    // program may have several variations of builders, each
    // implemented differently.
    '''

    def __init__(self):
        self._car = None

    def reset(self):
        '''
        // The reset method clears the object being built.
        '''

        self._car = Car()

    def set_seats(self, number_of_seats: int):
        '''
        // All production steps work with the same product instance.

        // Set the number of seats in the car
        '''
        self._car.seats = number_of_seats


    def set_engine(self, engine: Engine):
        '''
        // Install a given engine.
        '''
        self._car.engine = engine

    def set_trip_computer(self, trip_computer: bool):
        '''
        // Install a trip computer.
        '''
        self._car.trip_computer = trip_computer

    def set_gps(self, gps: bool):
        '''
        // Install a global positioning system.
        '''
        self._car.gps = gps

    def get_product(self) -> Car:
        '''
        // Concrete builders are supposed to provide their own
        // methods for retrieving results. That's because various
        // types of builders may create entirely different products
        // that don't all follow the same interface. Therefore such
        // methods can't be declared in the builder interface (at
        // least not in a statically-typed programming language).
        //
        // Usually, after returning the end result to the client, a
        // builder instance is expected to be ready to start
        // producing another product. That's why it's a usual
        // practice to call the reset method at the end of the
        // `getProduct` method body. However, this behavior isn't
        // mandatory, and you can make your builder wait for an
        // explicit reset call from the client code before disposing
        // of the previous result.
        '''

        product = self._car
        self.reset()
        return product


class CarManualBuilder(Builder):
    '''
    // Unlike other creational patterns, builder lets you construct
    // products that don't follow the common interface.
    '''

    def __init__(self):
        self._manual = None

    def reset(self):
        '''
        // The reset method clears the object being built.
        '''

        self._manual = Manual()

    def set_seats(self, number_of_seats: int):
        '''
        // Document car seat features.
        '''
        self._manual.seats = f'Car contains {number_of_seats} seats'

    def set_engine(self, engine: Engine):
        '''
        // Add engine instructions.
        '''
        self._manual.engine = f'Car contains {engine}'

    def set_trip_computer(self, trip_computer: bool):
        '''
        // Add trip computer instructions.
        '''
        message = 'Car contains trip computer' if trip_computer else 'Car doesn\'t contain trip computer'
        self._manual.trip_computer = message

    def set_gps(self, gps: bool):
        '''
         // Add GPS instructions.
        '''
        message = 'Car contains GPS' if gps else 'Car doesn\'t contain GPS'
        self._manual.gps = message

    def get_product(self) -> Car:
        '''
        // Return the manual and reset the builder.
        '''

        product = self._manual
        self.reset()
        return product
