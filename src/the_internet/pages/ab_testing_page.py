"""
A/B Testing page module.
"""

from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class ABTestingPage(BasePage):
    """
    A class to represent A/B Testing page.
    """

    _AB_PAGE_TITLE = (By.XPATH, "//div[@class='example']/h3")

    def get_abtest_page(self) -> None:
        """
        Open page.

        :return: None
        """

        return self.driver.get(f"{self.url}/abtest")

    def abtest_page_title_text(self) -> str:
        """
        Get title text.

        :return: Title text
        """

        return self.get_element_text(self._AB_PAGE_TITLE)

    def abtest_page_reached(self) -> str:
        """
        Check if page is opened.

        :return: True or False
        """

        return self.element_is_present(self._AB_PAGE_TITLE)
