from selenium.common.exceptions import TimeoutException
from src.the_internet.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class DynamicControlsPage(BasePage):
    checkbox_loctor = (By.ID, "checkbox")
    add_remove_button_locator = (By.XPATH, "//form[@id='checkbox-example']/button")
    loader_locator = (By.ID, "loading")
    message_locator = (By.ID, "message")
    edit_field_locator = (By.XPATH, "//input[@type='text']")

    def get_dynamic_controls_page(self):
        return self.driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    def checkbox_is_present(self):
        try:
            checkbox_present = self.find_element(self.checkbox_loctor)
        except TimeoutException:
            checkbox_present = False
        return checkbox_present

    def click_add_remove_button(self):
        self.click_on_element(self.add_remove_button_locator)
        return self.wait_until_invisible(self.loader_locator)

    def message_has_text(self, text):
        return self.element_has_text(self.message_locator, text)

    def add_remove_button_has_caption(self, caption):
        return self.element_has_text(self.add_remove_button_locator, caption)

    def edit_field_is_disabled(self):
        """
        Verify if the field enabled/disabled
        :return: True if the field disabled; None if it's enabled
        """
        edit_field = self.find_element(self.edit_field_locator)
        is_disabled = edit_field.get_attribute("disabled")
        return is_disabled
