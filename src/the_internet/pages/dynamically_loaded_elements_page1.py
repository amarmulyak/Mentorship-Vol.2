from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class DynamicallyLoadedElementsPage1(BasePage):
    _START_BUTTON_SECTION = (By.XPATH, "//div[@id='start']")
    _START_BUTTON = (By.XPATH, "//div[@id='start']/button")
    _DYNAMIC_TEXT_SECTION = (By.XPATH, "//div[@id='finish']")
    _DYNAMIC_TEXT = (By.XPATH, "//div[@id='finish']/h4")
    _LOADER = (By.ID, "loading")

    def get_dynamically_loaded_elements_page1(self):
        return self.driver.get(f"{self.path}/dynamic_loading/1")

    def start_button_is_displayed(self):
        return self._element_displayed(self._START_BUTTON_SECTION)

    def dynamic_text_is_displayed(self):
        return self.wait_until_visible(self._DYNAMIC_TEXT)
        # return self._element_displayed(self.dynamic_text_section_locator)

    def click_start_button(self):
        self.click_on_element(self._START_BUTTON)
        self.wait_until_invisible(self._LOADER)

    def start_button_caption(self):
        return self.element_text(self._START_BUTTON)

    def dynamic_text(self):
        return self.element_text(self._DYNAMIC_TEXT)

    def _element_displayed(self, locator):
        element = self.find_element(locator)
        style = element.get_attribute("style")
        if style == "display: none;":
            element_displayed = False
        else:
            element_displayed = True
        return element_displayed
