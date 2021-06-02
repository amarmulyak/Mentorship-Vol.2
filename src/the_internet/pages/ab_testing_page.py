from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class ABTestingPage(BasePage):
    _AB_PAGE_TITLE = (By.XPATH, "//div[@class='example']/h3")

    def get_abtest_page(self):
        return self.driver.get("https://the-internet.herokuapp.com/abtest")

    def abtest_page_title_equal(self, text):
        return self.element_text_equal(self._AB_PAGE_TITLE, text)

    def abtest_page_reached(self):
        return self.element_is_present(self._AB_PAGE_TITLE)
