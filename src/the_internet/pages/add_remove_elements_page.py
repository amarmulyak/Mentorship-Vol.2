from src.the_internet.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AddRemoveElementsPage(BasePage):
    add_element_btn = (By.XPATH, "//div[@class='example']/button")

    def get_add_remove_elements_page(self):
        return self.driver.get(self.base_url + "add_remove_elements/")

    def add_element(self):
        return self.click_on_element(self.add_element_btn)
