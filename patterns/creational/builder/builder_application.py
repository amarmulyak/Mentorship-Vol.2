'''
Application module
'''
from patterns.creational.builder.builder_director import Director
from patterns.creational.builder.builder_interface import CarBuilder, CarManualBuilder


class Application:
    '''
    // The client code creates a builder object, passes it to the
    // director and then initiates the construction process. The end
    // result is retrieved from the builder object.
    '''

    @staticmethod
    def make_car():
        '''
        # // The final product is often retrieved from a builder
        # // object since the director isn't aware of and not
        # // dependent on concrete builders and products.
        # Manual manual = builder.getProduct()
        '''
        director = Director()
        car_builder = CarBuilder()

        director.set_builder(car_builder)
        director.construct_sports_car()

        car = car_builder.get_product()

        car_manual_builder = CarManualBuilder()

        director.set_builder(car_manual_builder)
        director.construct_sports_car()

        manual = car_manual_builder.get_product()

        return car, manual


appl = Application()
s_c = appl.make_car()
