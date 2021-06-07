from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage
from src.the_internet.pages.dynamically_loaded_elements_page_e1 import DynamicallyLoadedElementsPageE1
from src.the_internet.pages.dynamically_loaded_elements_page_e2 import DynamicallyLoadedElementsPageE2


class DynamicallyLoadedElementsPage(BasePage):
    _EXAMPLE_1_LINK = (By.XPATH, "//a[contains(text(), 'Example 1')]")
    _EXAMPLE_2_LINK = (By.XPATH, "//a[contains(text(), 'Example 2')]")

    def page_is_reached(self):
        return self.element_is_present(self._EXAMPLE_1_LINK)

    def click_example_1_link(self):
        self.click_on_element(self._EXAMPLE_1_LINK)
        return DynamicallyLoadedElementsPageE1(self.driver, self.url)

    def click_example_2_link(self):
        self.click_on_element(self._EXAMPLE_2_LINK)
        return DynamicallyLoadedElementsPageE2(self.driver, self.url)