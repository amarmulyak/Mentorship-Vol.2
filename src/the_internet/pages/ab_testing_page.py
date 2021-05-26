from src.the_internet.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ABTestingPage(BasePage):
    ab_page_title_locator = (By.XPATH, "//div[@class='example']/h3")

    def get_abtest_page(self):
        return self.driver.get("https://the-internet.herokuapp.com/abtest")

    def abtest_page_title_has_text(self, text):
        return self.element_has_text(self.ab_page_title_locator, text)
