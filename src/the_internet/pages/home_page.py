from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage
from src.the_internet.pages.ab_testing_page import ABTestingPage


class HomePage(BasePage):
    # TODO Додати переходи на дочірні сторінки + вертати інстанси пейджі
    home_page_title_locator = (By.CLASS_NAME, "heading")
    ab_testing_link_locator = (By.XPATH, "//a[contains(text(), 'A/B Testing')]")
    example_link_locator = (By.XPATH, "//a[contains(text(), '{}')]")

    def get_home_page(self):
        return self.driver.get("https://the-internet.herokuapp.com/")

    def home_page_title_equal(self, text):
        return self.element_text_equal(self.home_page_title_locator, text)

    def click_ab_testing_link(self):
        self.click_on_element((
            self.example_link_locator[0],
            self.example_link_locator[1].format("A/B Testing")
        ))
        return ABTestingPage(self.driver)
