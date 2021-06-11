from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class DynamicallyLoadedElementsPageE1(BasePage):
    _START_BUTTON = (By.XPATH, "//div[@id='start']/button")
    _DYNAMIC_TEXT = (By.XPATH, "//div[@id='finish']/h4")
    _LOADER = (By.ID, "loading")

    def get_dynamically_loaded_elements_page1(self):
        return self.driver.get(f"{self.url}/dynamic_loading/1")

    def page_is_reached(self):
        return self.element_is_present(self._START_BUTTON)

    def start_button_is_visible(self, wait_time=10):
        return self.element_is_visible(self._START_BUTTON, wait_time)

    def dynamic_text_is_visible(self, wait_time=10):
        return self.element_is_visible(self._DYNAMIC_TEXT, wait_time)

    def click_start_button(self):
        self.click_on_element(self._START_BUTTON)
        self.wait_until_invisible(self._LOADER)

    def start_button_caption(self):
        return self.get_element_text(self._START_BUTTON)

    def dynamic_text(self):
        return self.get_element_text(self._DYNAMIC_TEXT)
