from src.the_internet.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException


class BasicAuthPage(BasePage):
    basic_auth_title = BasePage.page_title_locator

    def get_basic_auth_page(self, username, password):
        url = "the-internet.herokuapp.com/basic_auth"
        username = username
        password = password
        return self.driver.get(f"https://{username}:{password}@{url}")

    # def check_basic_auth_title(self):
    #     self.check_element_text(self.basic_auth_title, "Basic Auth")

    def check_basic_auth_title(self):
        title_found = False
        try:
            title_found = self.check_element_text(self.basic_auth_title, "Basic Auth")
        except TimeoutException:
            pass
        return title_found
