from src.the_internet.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException


class BasicAuthPage(BasePage):
    basic_auth_title_locator = BasePage.page_title_locator

    def get_basic_auth_page(self, username, password):
        url = "the-internet.herokuapp.com/basic_auth"
        username = username
        password = password
        return self.driver.get(f"https://{username}:{password}@{url}")

    def basic_auth_title_equal(self, text):
        return self.element_text_equal(self.basic_auth_title_locator, text)

    def basic_auth_page_reached(self, wait_time=10):
        return self.element_is_present(self.basic_auth_title_locator, wait_time)
