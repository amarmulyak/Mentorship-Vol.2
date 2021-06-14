from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class DynamicControlsPage(BasePage):
    _CHECKBOX = (By.ID, "checkbox")
    _CHECKBOX_ADD_REMOVE_BUTTON = (By.XPATH, "//form[@id='checkbox-example']/button")
    _CHECKBOX_LOADER = (By.XPATH, "//form[@id='checkbox-example']/div[@id='loading']")
    _CHECKBOX_MESSAGE = (By.XPATH, "//form[@id='checkbox-example']/p[@id='message']")
    _INPUT_LOADER = (By.XPATH, "//form[@id='input-example']/div[@id='loading']")
    _INPUT_FIELD = (By.XPATH, "//input[@type='text']")
    _INPUT_ENABLE_DISABLE_BTN = (By.XPATH, "//form[@id='input-example']/button")
    _INPUT_MESSAGE = (By.XPATH, "//form[@id='input-example']/p[@id='message']")

    def get_dynamic_controls_page(self):
        return self.driver.get(f"{self.url}/dynamic_controls")

    def checkbox_is_present(self, wait_time=10):
        return self.element_is_present(self._CHECKBOX, wait_time)

    def click_add_remove_button(self):
        self.click_on_element(self._CHECKBOX_ADD_REMOVE_BUTTON)
        return self.wait_until_invisible(self._CHECKBOX_LOADER)

    def checkbox_message_text(self):
        return self.get_element_text(self._CHECKBOX_MESSAGE)

    def add_remove_button_caption(self):
        return self.get_element_text(self._CHECKBOX_ADD_REMOVE_BUTTON)

    def input_field_is_disabled(self):
        edit_field = self.find_element(self._INPUT_FIELD)
        return bool(edit_field.get_attribute("disabled"))

    def enable_disable_button_caption(self):
        return self.get_element_text(self._INPUT_ENABLE_DISABLE_BTN)

    def click_enable_disable_button(self):
        self.click_on_element(self._INPUT_ENABLE_DISABLE_BTN)
        return self.wait_until_invisible(self._INPUT_LOADER)

    def input_message_text(self):
        return self.get_element_text(self._INPUT_MESSAGE)
