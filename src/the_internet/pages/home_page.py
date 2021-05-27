from src.the_internet.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    # TODO Додати переходи на дочірні сторінки + вертати інстанси пейджі
    home_page_title_locator = (By.CLASS_NAME, "heading")
    ab_testing_link_locator = (By.XPATH, "//a[contains(@href, '/abtest')]")

    def get_home_page(self):
        return self.driver.get("https://the-internet.herokuapp.com/")

    def home_page_title_equal(self, text):
        return self.element_text_equal(self.home_page_title_locator, text)
