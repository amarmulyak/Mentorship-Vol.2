from src.the_internet.pages.authentication import Authentication


class DigestAuthPage(Authentication):

    def get_digest_auth_page(self, username, password):
        return self._get_auth_page(username, password, last_segment="digest_auth")
