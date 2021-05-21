from src.the_internet.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ABTestingPage(BasePage):
    ab_page_title = (By.XPATH, "//div[@class = 'example']/h3")

    def get_abtest_page(self):
        return self.driver.get(self.base_url + "abtest")

    def check_abtest_page_title(self):
        return self.check_element_text(self.ab_page_title, "A/B Test Variation 1")
