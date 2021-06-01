from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class DynamicControlsPage(BasePage):
    checkbox_loctor = (By.ID, "checkbox")
    checkbox_add_remove_button_locator = (By.XPATH, "//form[@id='checkbox-example']/button")
    checkbox_loader_locator = (By.XPATH, "//form[@id='checkbox-example']/div[@id='loading']")
    checkbox_message_locator = (By.XPATH, "//form[@id='checkbox-example']/p[@id='message']")
    input_loader_locator = (By.XPATH, "//form[@id='input-example']/div[@id='loading']")
    input_field_locator = (By.XPATH, "//input[@type='text']")
    input_enable_disable_btn_locator = (By.XPATH, "//form[@id='input-example']/button")
    input_message_locator = (By.XPATH, "//form[@id='input-example']/p[@id='message']")

    def get_dynamic_controls_page(self):
        return self.driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    def checkbox_is_present(self, wait_time=10):
        return self.element_is_present(self.checkbox_loctor, wait_time)

    def click_add_remove_button(self):
        self.click_on_element(self.checkbox_add_remove_button_locator)
        return self.wait_until_invisible(self.checkbox_loader_locator)

    def checkbox_message_equal(self, text):
        return self.element_text_equal(self.checkbox_message_locator, text)

    def add_remove_button_caption_equal(self, caption):
        return self.element_text_equal(self.checkbox_add_remove_button_locator, caption)

    def input_field_is_disabled(self):
        edit_field = self.find_element(self.input_field_locator)
        if edit_field.get_attribute("disabled"):
            is_disabled = True
        else:
            is_disabled = False
        return is_disabled

    def enable_disable_button_caption_equal(self, caption):
        return self.element_text_equal(self.input_enable_disable_btn_locator, caption)

    def click_enable_disable_button(self):
        self.click_on_element(self.input_enable_disable_btn_locator)
        return self.wait_until_invisible(self.input_loader_locator)

    def input_message_equal(self, text):
        return self.element_text_equal(self.input_message_locator, text)

