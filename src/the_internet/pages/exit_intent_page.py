from selenium.webdriver.common.by import By
from src.the_internet.pages.entry_ad_page import EntryAd
import pyautogui


# TODO Робити спільні пейджі від яких наслідуватись
class ExitIntent(EntryAd):
    _TITLE = EntryAd._PAGE_TITLE
    _POWERED_BY = (By.XPATH, "//a[@target]")

    def get_entry_exit_intent_page(self):
        self.driver.get(f"{self.url}/exit_intent")

    def move_mouse_out_of_viewport(self):
        pyautogui.moveTo(500, 500)
        pyautogui.moveTo(500, 0)

# TODO апдейтити requirenents