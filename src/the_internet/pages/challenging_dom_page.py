from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class ChallengingDomPage(BasePage):
    answer_locator = (By.ID, "canvas")
    answer_text_locaotr = (By.XPATH, "//script/text()")
    cell_data_locator = (
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
                self.cell_data_locator[0],
                self.cell_data_locator[1].format(row_number, title_name),
            )
        ).text
