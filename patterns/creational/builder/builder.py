'''
// Using the Builder pattern makes sense only when your products
// are quite complex and require extensive configuration. The
// following two products are related, although they don't have
// a common interface.
'''
class Car:
    '''
    // A car can have a GPS, trip computer and some number of
    // seats. Different models of cars (sports car, SUV,
    // cabriolet) might have different features installed or
    // enabled.
    '''


class Manual:
    '''
    // Each car should have a user manual that corresponds to
    // the car's configuration and describes all its features.
    '''
