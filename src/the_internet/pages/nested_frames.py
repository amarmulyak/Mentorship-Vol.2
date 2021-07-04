"""
Nested Frames module.
"""

from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class NestedFramesPage(BasePage):
    """
    Class to represent Nested Frames page.
    """

    FRAME_TEXT = (By.XPATH, "//body")

    def get_nested_frames_page(self) -> None:
        """
        Open Nested Frames page.

        :return: None
        """

        self.driver.get(f"{self.url}/nested_frames")

    def get_frame_text(self) -> str:
        """
        Get text from the frame.

        :return: Text
        """

        return self.get_element_text(self.FRAME_TEXT)

    def switch_to_left_frame(self) -> None:
        """
        Switch to the left frame.

        :return: None
        """

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("frame-top")
        self.driver.switch_to.frame("frame-left")

    def switch_to_middle_frame(self) -> None:
        """
        Switch to the middle frame.

        :return: None
        """

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("frame-top")
        self.driver.switch_to.frame("frame-middle")

    def switch_to_right_frame(self) -> None:
        """
        Switch to the right frame.

        :return: None
        """

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("frame-top")
        self.driver.switch_to.frame("frame-right")

    def switch_to_bottom_frame(self) -> None:
        """
        Switch to the bottom frame.

        :return: None
        """

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("frame-bottom")
