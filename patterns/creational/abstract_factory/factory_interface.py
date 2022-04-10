'''
Docsting
'''

from abc import ABCMeta, abstractmethod


class Button(metaclass=ABCMeta):
    '''
    // Each distinct product of a product family should have a base
    // interface. All variants of the product must implement this
    // interface.
    '''

    @abstractmethod
    def paint(self):
        '''
        Docsting
        '''


class WinButton(Button):
    '''
    // Concrete products are created by corresponding concrete
    // factories.
    '''

    def paint(self):
        '''
        // Render a button in Windows style.
        '''
        # pass
        return "WinButton -> Paint"


class MacButton(Button):
    '''
    Docsting
    '''

    def paint(self):
        '''
        // Render a button in macOS style.
        '''
        # pass
        return "MacButton -> Paint"


class Checkbox:
    '''
    // Here's the base interface of another product. All products
    // can interact with each other, but proper interaction is
    // possible only between products of the same concrete variant.
    '''

    @abstractmethod
    def paint(self):
        '''
        Docsting
        '''


class WinCheckbox(Checkbox):
    '''
    Docsting
    '''

    def paint(self):
        '''
        // Render a checkbox in Windows style.
        '''
        # pass
        return "WinCheckbox -> Paint"


class MacCheckbox(Checkbox):
    '''
    Docsting
    '''

    def paint(self):
        '''
        // Render a checkbox in macOS style.
        '''
        # pass
        return "MacCheckbox -> Paint"
