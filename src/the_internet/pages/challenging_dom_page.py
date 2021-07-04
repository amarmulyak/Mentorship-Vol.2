"""
Challenging Dom module.
"""
from typing import Dict

from selenium.webdriver.common.by import By

from src.the_internet.pages.base_page import BasePage


class ChallengingDomPage(BasePage):
    """
    Class to represent Challenging Dom page.
    """

    _ANSWER = (By.ID, "canvas")
    _ANSWER_TEXT = (By.XPATH, "//script/text()")
    _CELL_DATA = (
        By.XPATH,
        "//div[@class='large-10 columns']/table/tbody/tr[position()={}]/"
        "td[position()=count(//div[@class='large-10 columns']/"
        "table/thead/tr/th[contains(., '{}')]/preceding-sibling::th)+1]"
    )

    def get_challenging_dom_page(self) -> None:
        """
        Open Challenging Dom page.

        :return: None
        """

        return self.driver.get(f"{self.url}/challenging_dom")

    def get_answer(self) -> Dict:
        """
        Get canvas.

        :return: Result of the script execution as Dictionary
        """

        answer = self.driver.execute_script("return canvas;")
        return answer

    def get_data_from_cell(self, row_number: int, title_name: str) -> str:
        """
        Get text from the cell.

        :param row_number: Number of the row
        :param title_name: Name of the column's title
        :return: Text
        """

        return self.find_element(
            (
                self._CELL_DATA[0],
                self._CELL_DATA[1].format(row_number, title_name),
            )
        ).text
