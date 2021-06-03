from src.the_internet.pages.base_page import BasePage


class DigestAuthPage(BasePage):
    _DIGEST_AUTH_TITLE = BasePage._PAGE_TITLE

    def get_basic_auth_page(self, username, password):
        url = "the-internet.herokuapp.com/digest_auth"
        username = username
        password = password
        return self.driver.get(f"https://{username}:{password}@{url}")

    def digest_auth_title_text(self):
        return self.element_text(self._DIGEST_AUTH_TITLE)

    def digest_auth_page_reached(self, wait_time=10):
        return self.element_is_present(self._DIGEST_AUTH_TITLE, wait_time)
