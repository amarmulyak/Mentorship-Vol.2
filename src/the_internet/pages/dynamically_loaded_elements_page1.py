from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class DynamicallyLoadedElementsPage1(BasePage):
    # TODO Зробити капсом і протектед
    start_button_section_locator = (By.XPATH, "//div[@id='start']")
    start_button_locator = (By.XPATH, "//div[@id='start']/button")
    dynamic_text_section_locator = (By.XPATH, "//div[@id='finish']")
    dynamic_text_locator = (By.XPATH, "//div[@id='finish']/h4")
    loader_locator = (By.ID, "loading")

    def get_dynamically_loaded_elements_page1(self):
        return self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    def start_button_is_displayed(self):
        return self._element_displayed(self.start_button_section_locator)

    def dynamic_text_is_displayed(self):
        return self.wait_until_visible(self.dynamic_text_locator)
        # return self._element_displayed(self.dynamic_text_section_locator)

    def click_start_button(self):
        self.click_on_element(self.start_button_locator)
        self.wait_until_invisible(self.loader_locator)

    def start_button_caption_equal(self, text):
        return self.element_text_equal(self.start_button_locator, text)

    def dynamic_text_equal(self, text):
        return self.element_text_equal(self.dynamic_text_locator, text)

    def _element_displayed(self, locator):
        element = self.find_element(locator)
        style = element.get_attribute("style")
        if style == "display: none;":
            element_displayed = False
        else:
            element_displayed = True
        return element_displayed
