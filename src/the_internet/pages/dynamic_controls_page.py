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
        return self.driver.get(self.base_url + "dynamic_controls")

    def verify_checkbox_present(self, expected: bool):
        try:
            self.find_element(self.checkbox_loctor)
            checkbox_present = True
        except TimeoutException:
            checkbox_present = False
        assert checkbox_present == expected

    def click_add_remove_button(self):
        self.click_on_element(self.add_remove_button_locator)
        return self.wait_until_invisible(self.loader_locator)

    def check_message_text(self, text):
        return self.check_element_text(self.message_locator, text)

    def check_add_remove_button_caption(self, caption):
        return self.check_element_text(self.add_remove_button_locator, caption)

    def check_edit_field_enabled(self):
        # How to check properly if the field is enabled
        edit_field = self.find_element(self.edit_field_locator)
        enabled = edit_field.get_attribute("disabled")  # Returns None if the field is enabled
        return enabled
