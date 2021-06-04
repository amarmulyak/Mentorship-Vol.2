from selenium.webdriver.common.by import By
from seletools.actions import drag_and_drop
from src.the_internet.pages.base_page import BasePage


class DragAndDropPage(BasePage):
    _COLUMN_A = (By.XPATH, "//div[@id='column-a']")
    _COLUMN_B = (By.XPATH, "//div[@id='column-b']")

    def get_drag_and_drop_page(self):
        return self.driver.get(f"{self.url}/drag_and_drop")

    def column_a_text(self):
        return self.element_text(self._COLUMN_A)

    def column_b_text(self):
        return self.element_text(self._COLUMN_B)

    def drag_and_drop_column_a_to_b(self):
        return self._drag_and_drop(
            self._COLUMN_A,
            self._COLUMN_B
        )

    def drag_and_drop_column_b_to_a(self):
        return self._drag_and_drop(
            self._COLUMN_B,
            self._COLUMN_A
        )

    def _drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        drag_and_drop(self.driver, source, target)
