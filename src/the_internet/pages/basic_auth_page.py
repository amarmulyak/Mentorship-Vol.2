from src.the_internet.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException


class BasicAuthPage(BasePage):
    basic_auth_title_locator = BasePage.page_title_locator

    def get_basic_auth_page(self, username, password):
        url = "the-internet.herokuapp.com/basic_auth"
        username = username
        password = password
        return self.driver.get(f"https://{username}:{password}@{url}")

    def basic_auth_title_has_text(self, text):
        return self.element_has_text(self.basic_auth_title_locator, text)

    def basic_auth_page_reached(self):
        # TODO Має повертати Тру або Фолс + передавати час очікування
        try:
            title_found = self.find_element(self.basic_auth_title_locator)
        except TimeoutException:
            title_found = False
        return title_found
