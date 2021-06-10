from selenium.webdriver.common.by import By
from src.the_internet.pages.modal_page import ModalPage


class EntryAd(ModalPage):
    _RESTART_ADD = (By.ID, "restart-ad")

    def get_entry_ad_page(self):
        self.driver.get(f"{self.url}/entry_ad")

    def click_restart_add(self):
        return self.click_on_element(self._RESTART_ADD)
