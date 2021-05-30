from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class DynamicControlsPage(BasePage):
    checkbox_loctor = (By.ID, "checkbox")
    add_remove_button_locator = (By.XPATH, "//form[@id='checkbox-example']/button")
    loader_locator = (By.ID, "loading")
    message_locator = (By.ID, "message")
    edit_field_locator = (By.XPATH, "//input[@type='text']")

    def get_dynamic_controls_page(self):
        return self.driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    def checkbox_is_present(self, wait_time=10):
        return self.element_is_present(self.checkbox_loctor, wait_time)

    def click_add_remove_button(self):
        self.click_on_element(self.add_remove_button_locator)
        return self.wait_until_invisible(self.loader_locator)

    def message_equal(self, text):
        return self.element_text_equal(self.message_locator, text)

    def add_remove_button_has_caption(self, caption):
        return self.element_text_equal(self.add_remove_button_locator, caption)

    def edit_field_is_disabled(self):
        edit_field = self.find_element(self.edit_field_locator)
        if edit_field.get_attribute("disabled"):
            is_disabled = True
        else:
            is_disabled = False
        return is_disabled
