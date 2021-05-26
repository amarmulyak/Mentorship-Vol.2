from src.the_internet.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    # TODO Додати переходи на дочірні сторінки + вертати інстанси пейджі
    home_page_title = (By.CLASS_NAME, "heading")
    ab_testing_link = (By.XPATH, "//a[contains(@href, '/abtest')]")

    def get_home_page(self):
        return self.driver.get("https://the-internet.herokuapp.com/")

    def check_home_page_title(self):
        return self.check_element_text(self.home_page_title, "Welcome to the-internet")
