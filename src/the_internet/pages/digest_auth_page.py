from src.the_internet.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException


class DigestAuthPage(BasePage):
    digest_auth_title_locator = BasePage.page_title_locator

    def get_basic_auth_page(self, username, password):
        url = "the-internet.herokuapp.com/digest_auth"
        username = username
        password = password
        return self.driver.get(f"https://{username}:{password}@{url}")

    def digest_auth_title_has_text(self, text):
        return self.element_has_text(self.digest_auth_title_locator, text)

    def digest_auth_page_reached(self):
        try:
            title_found = self.find_element(self.digest_auth_title_locator)
        except TimeoutException:
            title_found = False
        return title_found
