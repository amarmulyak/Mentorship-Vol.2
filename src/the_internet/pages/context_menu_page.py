"""
Context Menu module.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from src.the_internet.pages.base_page import BasePage


class ContextMenuPage(BasePage):
    """
    Class to represent Context Menu page.
    """

    _BOX = (By.ID, "hot-spot")

    def get_context_menu_page(self) -> None:
        """
        Open Context Menu page.

        :return: None
        """

        return self.driver.get(f"{self.url}/context_menu")

    def right_mouse_click_on_box(self) -> None:
        """
        Click on the box with right mouse button.

        :return: None
        """

        box = self.find_element(self._BOX)
        action = ActionChains(self.driver)
        return action.context_click(box).perform()
