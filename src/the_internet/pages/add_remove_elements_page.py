"""
Add/Remove Elements module.
"""
import logging
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.the_internet.pages.base_page import BasePage


class AddRemoveElementsPage(BasePage):
    """
    A class to represent Add/Remove Elements page.
    """

    _ADD_ELEMENT_BTN = (By.XPATH, "//div[@class='example']/button")
    _DELETE_BTNS = (By.CLASS_NAME, "added-manually")
    _DELETE_BTN = (By.XPATH, "//div[@id='elements']/button[{}]")

    logger = logging.getLogger()

    def get_add_remove_elements_page(self) -> None:

        """
        Open page.

        :return: None
        """
        self.logger.info(f'{__class__.__name__}: Opening page "Add Remove Elements"')
        return self.driver.get(f"{self.url}/add_remove_elements/")

    def add_element(self) -> None:
        """
        Click on "Add Element" button.

        :return: None
        """
        self.logger.info(f'{__class__.__name__}: Adding element')

        return self.click_on_element(self._ADD_ELEMENT_BTN)

    def add_elements(self, number_of_elements: int) -> None:
        """
        Add specified number of elements.

        :param number_of_elements: Number of elements you want to add
        :return: None
        """

        self.logger.info(f"{__class__.__name__}: Adding {number_of_elements} elements")

        for _ in range(number_of_elements):
            self.add_element()

    def get_delete_buttons(self) -> List[WebElement]:
        """
        Get list of "Delete" buttons web elements.

        :return: List of "Delete" buttons web elements
        """

        self.logger.info(f"{__class__.__name__}: Getting list of delete buttons")

        return self.driver.find_elements(*self._DELETE_BTNS)

    def delete_button(self, button_index: int) -> None:
        """
        Click on "Delete" button with the specified index.

        :param button_index: index of "Delete" button, e.g. 0 is the
        index of the first button

        :return: None
        """

        self.logger.info(f"{__class__.__name__}: Deleting button with index {button_index}")

        button_position = button_index + 1
        self.click_on_element(
            (
                self._DELETE_BTN[0],
                self._DELETE_BTN[1].format(button_position),
            )
        )

    def delete_buttons(self) -> None:
        """Click on the all "Delete" buttons.

        :return: None
        """

        self.logger.info(f"{__class__.__name__}: Deleting all 'Delete' buttons")

        delete_btns = self.get_delete_buttons()
        if delete_btns:
            for btn in delete_btns:
                btn.click()
