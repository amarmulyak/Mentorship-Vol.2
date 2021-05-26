from src.the_internet.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class AddRemoveElementsPage(BasePage):
    add_element_btn_locator = (By.XPATH, "//div[@class='example']/button")
    delete_btns_locator = (By.CLASS_NAME, "added-manually")
    delete_btn_locator = (By.XPATH, "//div[@id='elements']/button[{}]")

    def get_add_remove_elements_page(self):
        return self.driver.get(self.base_url + "add_remove_elements/")

    def add_element(self):
        return self.click_on_element(self.add_element_btn_locator)

    def add_elements(self, number_of_elements: int):
        for number in range(number_of_elements):
            self.add_element()
        return

    def get_delete_buttons(self, **kwargs):
        # TODO Шукати елементи методом від драйвера
        delete_btns = []
        try:
            delete_btns = self.find_elements(self.delete_btns_locator, **kwargs)
        except TimeoutException:
            pass
        return delete_btns

    def check_buttons_quantity(self, btns_quantity, **kwargs):
        # TODO Винести всі ассерт мнетоди в тести, Чек методи до дупи можливо
        """

        :param btns_quantity: Expected number of buttons
        :param kwargs: Pass time argument to cut wait time
        :return: Assertion result
        """
        delete_btns = self.get_delete_buttons(**kwargs)
        assert len(delete_btns) == btns_quantity

    def delete_button(self, button_position):
        # TODO Видаляти батон на базі ліста гет_деліт_батонс
        self.click_on_element(
            (
                self.delete_btn_locator[0],
                self.delete_btn_locator[1].format(button_position),
            )
        )

    def delete_buttons(self):
        delete_btns = self.get_delete_buttons()
        if delete_btns:
            for btn in range(len(delete_btns)):
                self.delete_button(1)
