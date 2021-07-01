"""
Dynamically loaded elements - Example 1 module.
"""

from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class DynamicallyLoadedElementsPageE1(BasePage):
    """
    Class to represent Dynamically loaded elements - Example 1 page.
    """

    _START_BUTTON = (By.XPATH, "//div[@id='start']/button")
    _DYNAMIC_TEXT = (By.XPATH, "//div[@id='finish']/h4")
    _LOADER = (By.ID, "loading")

    def get_dynamically_loaded_elements_page1(self):
        """
        Open page.

        :return: None
        """

        return self.driver.get(f"{self.url}/dynamic_loading/1")

    def is_page_reached(self):
        """
        Check if page is reached.

        :return: True or False
        """

        return self.element_is_present(self._START_BUTTON)

    def is_start_button_visible(self, wait_time=10):
        """
        Check if "Start" button is visible.

        :param wait_time: Time
        :return: True or False
        """

        return self.element_is_visible(self._START_BUTTON, wait_time)

    def is_dynamic_text_visible(self, wait_time=10):
        """
        Check if dynamic text is visible.

        :param wait_time: Time
        :return: True or False
        """

        return self.element_is_visible(self._DYNAMIC_TEXT, wait_time)

    def click_start_button(self):
        """
        Clisk the "Start" button.

        :return: None
        """

        self.click_on_element(self._START_BUTTON)
        self.wait_until_invisible(self._LOADER)

    def get_start_button_caption(self):
        """
        Get "Start" button caption.

        :return: Button caption
        """

        return self.get_element_text(self._START_BUTTON)

    def get_dynamic_text(self):
        """
        Get dynamic text.

        :return: Dynamic text
        """

        return self.get_element_text(self._DYNAMIC_TEXT)
