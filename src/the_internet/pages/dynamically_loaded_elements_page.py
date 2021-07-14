"""
Dynamically loaded elements module.
"""

from selenium.webdriver.common.by import By

from src.the_internet.pages.base_page import BasePage
from src.the_internet.pages.dynamically_loaded_elements_page_e1 import DynamicallyLoadedElementsPageE1
from src.the_internet.pages.dynamically_loaded_elements_page_e2 import DynamicallyLoadedElementsPageE2


class DynamicallyLoadedElementsPage(BasePage):
    """
    Class to represent Dynamically Loaded Elements page.
    """

    _EXAMPLE_1_LINK = (By.XPATH, "//a[contains(text(), 'Example 1')]")
    _EXAMPLE_2_LINK = (By.XPATH, "//a[contains(text(), 'Example 2')]")

    def is_page_reached(self) -> bool:
        """
        Check if page is reached.

        :return: True or False
        """

        return self.element_is_present(self._EXAMPLE_1_LINK)

    def click_example_1_link(self) -> DynamicallyLoadedElementsPageE1:
        """
        Click "Example 1" link.

        :return: DynamicallyLoadedElementsPageE1
        """

        self.click_on_element(self._EXAMPLE_1_LINK)
        return DynamicallyLoadedElementsPageE1(self.driver)

    def click_example_2_link(self) -> DynamicallyLoadedElementsPageE2:
        """
        Click "Example 2" link.

        :return: DynamicallyLoadedElementsPageE2
        """

        self.click_on_element(self._EXAMPLE_2_LINK)
        return DynamicallyLoadedElementsPageE2(self.driver)
