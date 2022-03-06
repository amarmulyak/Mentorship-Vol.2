from patterns.creational.abstract_factory.factory import GUIFactory, WinFactory, MacFactory


class Application:
    '''
    // The client code works with factories and products only
    // through abstract types: GUIFactory, Button and Checkbox. This
    // lets you pass any factory or product subclass to the client
    // code without breaking it.
    '''

    def __init__(self, factory: GUIFactory):
        self._factory = factory

    def create_ui(self):
        self._button = self._factory.create_button()
        self._checkbox = self._factory.create_checkbox()

    def paint_button(self):
        self._button.paint()

    def paint_checkbox(self):
        self._checkbox.paint()


class ApplicationConfigurator:
    '''
    // The application picks the factory type depending on the
    // current configuration or environment settings and creates it
    // at runtime (usually at the initialization stage).
    '''

    def __init__(self, os):
        self.os = os

    def create_factory(self):
        if self.os == "Windows":
            factory = WinFactory()
        elif self.os == "Mac":
            factory = MacFactory()
        else:
            raise Exception("Error! Unknown operating system.")

        return Application(factory)

windows_app = ApplicationConfigurator(os='Windows').create_factory()
windows_app.create_ui()
windows_app.paint_button()
windows_app.paint_checkbox()

mac_app = ApplicationConfigurator(os='Mac').create_factory()
mac_app.create_ui()
mac_app.paint_button()
mac_app.paint_checkbox()
