"""
Drag and Drop page module.
"""

from selenium.webdriver.common.by import By

from src.the_internet.pages.base_page import BasePage


class DragAndDropPage(BasePage):
    """
    Class to represent Drag And Drop page.
    """

    _COLUMN_A = (By.XPATH, "//div[@id='column-a']")
    _COLUMN_B = (By.XPATH, "//div[@id='column-b']")

    def get_drag_and_drop_page(self):
        """
        Open Drag and Drop page.

        :return: None
        """

        return self.driver.get(f"{self.url}/drag_and_drop")

    def column_a_text(self):
        """
        Get Column A text.

        :return: Column A text
        """

        return self.get_element_text(self._COLUMN_A)

    def column_b_text(self):
        """
        Get Column B text.

        :return: Column B text
        """

        return self.get_element_text(self._COLUMN_B)

    def drag_and_drop_column_a_to_b(self):
        """
        Drag and drop column A to element B.

        :return: None
        """

        return self._drag_and_drop(self._COLUMN_A, self._COLUMN_B)

    def drag_and_drop_column_b_to_a(self):
        """
        Drag and drop column B to element A.

        :return: None
        """

        return self._drag_and_drop(self._COLUMN_B, self._COLUMN_A)
