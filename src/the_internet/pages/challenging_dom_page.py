from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class ChallengingDomPage(BasePage):
    _ANSWER = (By.ID, "canvas")
    _ANSWER_TEXT = (By.XPATH, "//script/text()")
    _CELL_DATA = (
        By.XPATH,
        "//div[@class='large-10 columns']/table/tbody/tr[position()={}]/td[position()=count(//div[@class='large-10 columns']/table/thead/tr/th[contains(., '{}')]/preceding-sibling::th)+1]",
    )

    def get_challenging_dom_page(self):
        return self.driver.get("https://the-internet.herokuapp.com/challenging_dom")

    def get_answer(self):
        answer = self.driver.execute_script("return canvas;")
        return answer

    def get_data_from_cell(self, row_number, title_name):
        return self.find_element(
            (
                self._CELL_DATA[0],
                self._CELL_DATA[1].format(row_number, title_name),
            )
        ).text
