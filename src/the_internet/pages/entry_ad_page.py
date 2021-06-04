from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class EntryAd(BasePage):
    _MODAL = (By.CLASS_NAME, "modal")
    _MODAL_TITLE = (By.CLASS_NAME, "modal-title")
    _MODAL_BODY = (By.CLASS_NAME, "modal-body")
    _MODAL_CLOSE_BTN = (By.XPATH, "//div[@class='modal-footer']/p")

    def get_entry_ad_page(self):
        self.driver.get(f"{self.url}/entry_ad")

    def modal_is_visible(self, wait_time=10):
        return self.element_is_visible(self._MODAL, wait_time=wait_time)

    def close_modal(self):
        self.click_on_element(self._MODAL_CLOSE_BTN)
        self.wait_until_invisible(self._MODAL)
