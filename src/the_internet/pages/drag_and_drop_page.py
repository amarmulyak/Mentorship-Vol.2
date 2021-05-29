from src.the_internet.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from seletools.actions import drag_and_drop


class DragAndDropPage(BasePage):
    element_a_locator = (By.XPATH, "//div[@id='column-a']")
    element_b_locator = (By.XPATH, "//div[@id='column-b']")

    def get_drag_and_drop_page(self):
        return self.driver.get("https://the-internet.herokuapp.com/drag_and_drop")

    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        drag_and_drop(self.driver, source, target)


