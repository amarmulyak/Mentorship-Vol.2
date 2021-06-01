from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class DynamicallyLoadedElementsPage1(BasePage):
    start_button_locator = (By.XPATH, "//div[@id='start']")
    dynmaic_text_locator = (By.XPATH, "//div[@id='finish']")

    def get_dynamically_loaded_elements_page1(self):
        return self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    def _element_displayed(self, locator):
        element = self.find_element(locator)
        style = element.get_attribute("style")
        if style == "display: none;":
            element_displayed = False
        else:
            element_displayed = True
        return element_displayed

    def start_button_is_displayed(self):
        return self._element_displayed(self.start_button_locator)

    def dynamic_text_is_displayed(self):
        return self._element_displayed(self.dynmaic_text_locator)
