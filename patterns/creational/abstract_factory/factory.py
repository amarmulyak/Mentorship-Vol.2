from abc import ABCMeta, abstractmethod

from patterns.creational.abstract_factory.interface import Button, Checkbox, WinButton, WinCheckbox, MacButton, \
    MacCheckbox


class GUIFactory(metaclass=ABCMeta):
    '''
    // The abstract factory interface declares a set of methods that
    // return different abstract products. These products are called
    // a family and are related by a high-level theme or concept.
    // Products of one family are usually able to collaborate among
    // themselves. A family of products may have several variants,
    // but the products of one variant are incompatible with the
    // products of another variant.
    '''

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WinFactory(GUIFactory):
    '''
    // Concrete factories produce a family of products that belong
    // to a single variant. The factory guarantees that the
    // resulting products are compatible. Signatures of the concrete
    // factory's methods return an abstract product, while inside
    // the method a concrete product is instantiated.
    '''

    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()


class MacFactory(GUIFactory):
    '''
    // Each concrete factory has a corresponding product variant.
    '''

    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()