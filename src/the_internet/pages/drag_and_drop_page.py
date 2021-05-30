from selenium.webdriver.common.by import By
from seletools.actions import drag_and_drop
from src.the_internet.pages.base_page import BasePage


class DragAndDropPage(BasePage):
    column_a_locator = (By.XPATH, "//div[@id='column-a']")
    column_b_locator = (By.XPATH, "//div[@id='column-b']")

    def get_drag_and_drop_page(self):
        return self.driver.get("https://the-internet.herokuapp.com/drag_and_drop")

    def column_a_text_equal(self, text):
        return self.element_text_equal(self.column_a_locator, text)

    def column_b_text_equal(self, text):
        return self.element_text_equal(self.column_b_locator, text)

    def drag_and_drop_column_a_to_b(self):
        return self._drag_and_drop(
            self.column_a_locator,
            self.column_b_locator
        )

    def drag_and_drop_column_b_to_a(self):
        return self._drag_and_drop(
            self.column_b_locator,
            self.column_a_locator
        )

    def _drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        drag_and_drop(self.driver, source, target)
