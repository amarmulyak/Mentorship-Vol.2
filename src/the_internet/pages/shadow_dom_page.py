from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class ShadowDomPage(BasePage):
    SHADOW_SECTION1 = (By.XPATH, "//span[@slot='my-text']")
    SHADOW_SECTION2_ROW1 = (By.XPATH, "//ul[@slot='my-text']/li[1]")
    SHADOW_SECTION2_ROW2 = (By.XPATH, "//ul[@slot='my-text']/li[2]")

    def get_shadow_dom_page(self):
        self.driver.get(f"{self.url}/shadowdom")

    def get_section1_text(self):
        return self.get_element_text(self.SHADOW_SECTION1)

    def get_section2_row1_text(self):
        return self.get_element_text(self.SHADOW_SECTION2_ROW1)

    def get_section2_row2_text(self):
        return self.get_element_text(self.SHADOW_SECTION2_ROW2)
