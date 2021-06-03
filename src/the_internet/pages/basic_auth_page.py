from src.the_internet.pages.base_page import BasePage


class BasicAuthPage(BasePage):
    _BASIC_AUTH_TITLE = BasePage._PAGE_TITLE

    def get_basic_auth_page(self, username, password):
        url = "the-internet.herokuapp.com/basic_auth"
        username = username
        password = password
        return self.driver.get(f"https://{username}:{password}@{url}")

    def basic_auth_title_text(self):
        return self.element_text(self._BASIC_AUTH_TITLE)

    def basic_auth_page_reached(self, wait_time=10):
        return self.element_is_present(self._BASIC_AUTH_TITLE, wait_time)
