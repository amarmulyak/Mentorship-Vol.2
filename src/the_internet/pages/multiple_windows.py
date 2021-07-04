"""
Multiple Windows module.
"""

from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class MultipleWindows(BasePage):
    """
    Class to represent Multiple Window.
    """

    _CLICK_HERE = (By.LINK_TEXT, "Click Here")

    def get_multiple_window_page(self) -> None:
        """
        Open Multiple Window page.

        :return: None
        """

        self.driver.get(f"{self.url}/windows")

    def click_on_click_here_link(self) -> None:
        """
        Click the "Click Here" link.

        :return: None
        """

        self.click_on_element(self._CLICK_HERE)

    def get_page_title(self) -> str:
        """
        Get text from the page title.

        :return: Text
        """

        return self.get_element_text(self._PAGE_TITLE)

    def count_open_windows(self) -> int:
        """
        Count the number of open windows (tabs).

        :return: Number of open windows
        """

        return len(self.driver.window_handles)

    def switch_to_next_window(self) -> None:
        """
        Switch to next window. If it's the last switch to the first.

        :return: None
        """

        current_window_index = self.driver.window_handles.index(self.driver.current_window_handle)
        last_window_index = self.driver.window_handles.index(self.driver.window_handles[-1])
        if current_window_index == last_window_index:
            next_window_handle = self.driver.window_handles[0]
        else:
            next_window_handle = self.driver.window_handles[current_window_index+1]
        self.driver.switch_to_window(next_window_handle)

    def switch_to_previous_window(self) -> None:
        """
        Switch to the previous window. If it's the first switch
        to the last.

        :return: None
        """

        current_window_index = self.driver.window_handles.index(self.driver.current_window_handle)
        if current_window_index == 0:
            previous_window_handle = self.driver.window_handles[-1]
        else:
            previous_window_handle = self.driver.window_handles[current_window_index-1]
        self.driver.switch_to_window(previous_window_handle)
