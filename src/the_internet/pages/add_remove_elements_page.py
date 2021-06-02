from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class AddRemoveElementsPage(BasePage):
    _ADD_ELEMENT_BTN = (By.XPATH, "//div[@class='example']/button")
    _DELETE_BTNS = (By.CLASS_NAME, "added-manually")
    _DELETE_BTN = (By.XPATH, "//div[@id='elements']/button[{}]")

    def get_add_remove_elements_page(self):
        return self.driver.get(
            f"{self.path}/add_remove_elements/"
        )

    def add_element(self):
        return self.click_on_element(self._ADD_ELEMENT_BTN)

    def add_elements(self, number_of_elements: int):
        for number in range(number_of_elements):
            self.add_element()

    def get_delete_buttons(self):
        return self.driver.find_elements(*self._DELETE_BTNS)

    def delete_button(self, button_position):
        self.click_on_element(
            (
                self._DELETE_BTN[0],
                self._DELETE_BTN[1].format(button_position),
            )
        )

    def delete_buttons(self):
        delete_btns = self.get_delete_buttons()
        if delete_btns:
            for btn in delete_btns:
                btn.click()
