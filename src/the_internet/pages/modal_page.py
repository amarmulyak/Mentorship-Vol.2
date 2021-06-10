from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class ModalPage(BasePage):
    _MODAL = (By.CLASS_NAME, "modal")
    _MODAL_TITLE = (By.XPATH, "//div[@class='modal-title']/h3")
    _MODAL_BODY = (By.XPATH, "//div[@class='modal-body']/p")
    _MODAL_CLOSE_BTN = (By.XPATH, "//div[@class='modal-footer']/p")

    def modal_is_visible(self, wait_time=10):
        return self.element_is_visible(self._MODAL, wait_time=wait_time)

    def close_modal(self):
        self.wait_until_element_clickable(self._MODAL_CLOSE_BTN)
        self.click_on_element(self._MODAL_CLOSE_BTN)
        self.wait_until_invisible(self._MODAL)

    def get_modal_title_text(self):
        self.wait_until_visible(self._MODAL)
        return self.element_text(self._MODAL_TITLE)

    def get_modal_body_text(self):
        self.wait_until_visible(self._MODAL)
        return self.element_text(self._MODAL_BODY)
