from src.the_internet.pages.authentication import Authentication


class BasicAuthPage(Authentication):
    def get_basic_auth_page(self, username, password):
        return self._get_auth_page(username, password, last_segment="basic_auth")
