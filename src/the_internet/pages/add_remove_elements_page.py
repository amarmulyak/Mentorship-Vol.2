from src.the_internet.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AddRemoveElementsPage(BasePage):
    add_element_btn_locator = (By.XPATH, "//div[@class='example']/button")
    delete_btns_locator = (By.CLASS_NAME, "added-manually")
    delete_btn_locator = (By.XPATH, "//div[@id='elements']/button[{}]")

    def get_add_remove_elements_page(self):
        return self.driver.get(
            "https://the-internet.herokuapp.com/add_remove_elements/"
        )

    def add_element(self):
        return self.click_on_element(self.add_element_btn_locator)

    def add_elements(self, number_of_elements: int):
        for number in range(number_of_elements):
            self.add_element()

    def get_delete_buttons(self):
        return self.driver.find_elements(*self.delete_btns_locator)

    def delete_button(self, button_position):
        self.click_on_element((self.delete_btn_locator[0],
                               self.delete_btn_locator[1].format(button_position)))

    def delete_buttons(self):
        delete_btns = self.get_delete_buttons()
        if delete_btns:
            for btn in delete_btns:
                btn.click()
