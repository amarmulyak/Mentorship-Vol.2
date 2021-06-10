import pyautogui
from src.the_internet.pages.modal_page import ModalPage


class ExitIntent(ModalPage):
    def get_entry_exit_intent_page(self):
        self.driver.get(f"{self.url}/exit_intent")

    def move_mouse_out_of_viewport(self):
        pyautogui.moveTo(500, 500)
        pyautogui.moveTo(500, 0)

# TODO апдейтити requirenents