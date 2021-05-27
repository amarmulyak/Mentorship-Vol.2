from src.the_internet.pages.base_page import BasePage


class DigestAuthPage(BasePage):
    digest_auth_title_locator = BasePage.page_title_locator

    def get_basic_auth_page(self, username, password):
        url = "the-internet.herokuapp.com/digest_auth"
        username = username
        password = password
        return self.driver.get(f"https://{username}:{password}@{url}")

    def digest_auth_title_equal(self, text):
        return self.element_text_equal(self.digest_auth_title_locator, text)

    def digest_auth_page_reached(self, wait_time=10):
        return self.element_is_present(self.digest_auth_title_locator, wait_time)
