"""
Digest Authentication module.
"""

from src.the_internet.pages.authentication import Authentication


class DigestAuthPage(Authentication):
    """
    Class to represent Digest Authentication page.
    """

    def get_digest_auth_page(self, username, password):
        """
        Open Digest Authentication page.

        :param username: Username
        :param password: Password
        :return: None
        """

        return self._get_auth_page(username, password, last_segment="digest_auth")
