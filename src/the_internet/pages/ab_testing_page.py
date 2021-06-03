from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class ABTestingPage(BasePage):
    _AB_PAGE_TITLE = (By.XPATH, "//div[@class='example']/h3")

    def get_abtest_page(self):
        return self.driver.get(f"{self.path}/abtest")

    def abtest_page_title_text(self):
        return self.element_text(self._AB_PAGE_TITLE)

    def abtest_page_reached(self):
        return self.element_is_present(self._AB_PAGE_TITLE)
