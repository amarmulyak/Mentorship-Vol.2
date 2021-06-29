"""
Basic Authentication module.
"""

from src.the_internet.pages.authentication import Authentication


class BasicAuthPage(Authentication):
    """
    A class to represent Basic Authentication page.
    """
    def get_basic_auth_page(self, username, password):
        """
        Open page.

        :param username: Username
        :param password: Password
        :return: None
        """
        return self._get_auth_page(username, password, last_segment="basic_auth")
