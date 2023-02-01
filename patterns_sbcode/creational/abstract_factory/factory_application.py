'''
Docsting
'''

from patterns_sbcode.creational.abstract_factory.factory import GUIFactory, WinFactory, MacFactory


class Application:
    '''
    // The client code works with factories and products only
    // through abstract types: GUIFactory, Button and Checkbox. This
    // lets you pass any factory or product subclass to the client
    // code without breaking it.
    '''

    def __init__(self, factory: GUIFactory):
        self._factory = factory
        self._button = self._factory.create_button()
        self._checkbox = self._factory.create_checkbox()

    def paint_button(self):
        '''
        Docsting
        '''

        return self._button.paint()

    def paint_checkbox(self):
        '''
        Docsting
        '''

        return self._checkbox.paint()


class ApplicationConfigurator:
    '''
    // The application picks the factory type depending on the
    // current configuration or environment settings and creates it
    // at runtime (usually at the initialization stage).
    '''

    def __init__(self, o_s):
        self.o_s = o_s

    def create_factory(self) -> Application:
        '''
        Docsting
        '''

        if self.o_s == "Windows":
            factory = WinFactory()
        elif self.o_s == "Mac":
            factory = MacFactory()
        else:
            raise Exception("Error! Unknown operating system.")

        return Application(factory)


windows_app = ApplicationConfigurator(o_s='Windows').create_factory()
print(windows_app.paint_button())
print(windows_app.paint_checkbox())

mac_app = ApplicationConfigurator(o_s='Mac').create_factory()
print(mac_app.paint_button())
print(mac_app.paint_checkbox())
