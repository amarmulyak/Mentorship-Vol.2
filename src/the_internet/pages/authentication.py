from src.the_internet.pages.base_page import BasePage


class Authentication(BasePage):
    _TITLE = BasePage._PAGE_TITLE

    def _get_auth_page(self, username, password, last_segment):
        domain = self.url.split("https://")[1]
        url = f"{domain}/{last_segment}"
        username = username
        password = password
        return self.driver.get(f"https://{username}:{password}@{url}")

    def title_text(self):
        return self.element_text(self._TITLE)

    def page_reached(self, wait_time=10):
        return self.element_is_present(self._TITLE, wait_time)
