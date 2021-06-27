from src.the_internet.pages.modal_page import ModalPage
from src.utils.utils import move_mouse_to


class ExitIntent(ModalPage):
    def get_entry_exit_intent_page(self):
        self.driver.get(f"{self.url}/exit_intent")

    def move_mouse_out_of_viewport(self):
        move_mouse_to(500, 500)
        move_mouse_to(500, 0)
