from src.the_internet.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ChallengingDomPage(BasePage):
    answer_locator = (By.ID, "canvas")
    answer_text_locaotr = (By.XPATH, '//script/text()')

    def get_challenging_dom_page(self):
        return self.driver.get(self.base_url + "challenging_dom")

    def get_answer(self):
        answer = self.driver.execute_script("return canvas;")
        return answer
