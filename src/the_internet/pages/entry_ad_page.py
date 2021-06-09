from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class EntryAd(BasePage):
    _MODAL = (By.CLASS_NAME, "modal")
    _MODAL_TITLE = (By.XPATH, "//div[@class='modal-title']/h3")
    _MODAL_BODY = (By.XPATH, "//div[@class='modal-body']/p")
    _MODAL_CLOSE_BTN = (By.XPATH, "//div[@class='modal-footer']/p")
    _RESTART_ADD = (By.ID, "restart-ad")

    def get_entry_ad_page(self):
        self.driver.get(f"{self.url}/entry_ad")

    def modal_is_visible(self, wait_time=10):
        return self.element_is_visible(self._MODAL, wait_time=wait_time)

    def close_modal(self):
        self.click_on_element(self._MODAL_CLOSE_BTN)
        self.wait_until_invisible(self._MODAL)

    # TODO Спробувати @property там де вертати текст (або перезвати метод + get)
    def modal_title_text(self):
        self.wait_until_visible(self._MODAL)
        return self.element_text(self._MODAL_TITLE)

    def modal_body_text(self):
        self.wait_until_visible(self._MODAL)
        return self.element_text(self._MODAL_BODY)

    def click_restart_add(self):
        return self.click_on_element(self._RESTART_ADD)
