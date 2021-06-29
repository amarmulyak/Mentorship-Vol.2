"""
Authentication module.
"""

from src.the_internet.pages.base_page import BasePage


class Authentication(BasePage):
    """
    A class to represent Authentication page.
    """

    _TITLE = BasePage._PAGE_TITLE

    def _get_auth_page(self, username, password, last_segment):
        """
        Get page with basic authentication required

        :param username: Usermame
        :param password: Password
        :param last_segment: Last segment of the URL
        :return: None
        """

        domain = self.url.split("https://")[1]
        url = f"{domain}/{last_segment}"
        return self.driver.get(f"https://{username}:{password}@{url}")

    def title_text(self):
        """
        Get title text

        :return: Title text
        """

        return self.get_element_text(self._TITLE)

    def page_reached(self, wait_time=10):
        """
        Check if page is reached

        :param wait_time: time (default is 10)
        :return: True or False
        """

        return self.element_is_present(self._TITLE, wait_time)
