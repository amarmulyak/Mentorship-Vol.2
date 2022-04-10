'''
// The director is only responsible for executing the building
// steps in a particular sequence. It's helpful when producing
// products according to a specific order or configuration.
// Strictly speaking, the director class is optional, since the
// client can control builders directly.
'''

from patterns.creational.builder.builder_module import SportEngine, RegularEngine
from patterns.creational.builder.builder_interface import Builder


class Director:
    '''
    Class Director
    '''

    def __init__(self):
        self._builder = None


    def set_builder(self, builder: Builder):
        '''
        // The director works with any builder instance that the
        // client code passes to it. This way, the client code may
        // alter the final type of the newly assembled product.
        '''

        self._builder = builder

    def construct_sports_car(self):
        '''
        // The director can construct several product variations
        // using the same building steps.
        '''
        self._builder.reset()
        self._builder.set_seats(2)
        self._builder.set_engine(SportEngine())
        self._builder.set_trip_computer(True)
        self._builder.set_gps(True)

    def construct_suv(self):
        '''
        Method to construct SUV
        '''
        self._builder.reset()
        self._builder.set_seats(5)
        self._builder.set_engine(RegularEngine())
        self._builder.set_trip_computer(False)
        self._builder.set_gps(False)
