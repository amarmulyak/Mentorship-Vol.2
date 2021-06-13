from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class MultipleWindow(BasePage):
    CLICK_HERE = (By.LINK_TEXT, "Click Here")

    def get_multiple_window_page(self):
        self.driver.get(f"{self.url}/windows")

    def click_on_click_here_button(self):
        self.click_on_element(self.CLICK_HERE)

    def get_page_title(self):
        return self.get_element_text(self._PAGE_TITLE)
