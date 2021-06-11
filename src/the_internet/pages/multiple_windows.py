from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class MultipleWindow(BasePage):
    CLICK_HERE = (By.LINK_TEXT, "Click Here")

    def get_multiple_window_page(self):
        self.driver.get(f"{self.url}/windows")
