from src.the_internet.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class DragAndDropPage(BasePage):
    column_a_locator = (By.XPATH, "//div[@id='column-a']")
    column_b_locator = (By.XPATH, "//div[@id='column-b']")

    def get_drag_and_drop_page(self):
        return self.driver.get("https://the-internet.herokuapp.com/drag_and_drop")

    def drag_and_drop_column_a_to_b(self):
        # TODO Попробувати бібліотеку drag_and_drop
        a = self.find_element(self.column_a_locator)
        b = self.find_element(self.column_b_locator)
        action_chains = ActionChains(self.driver)
        # action_chains.drag_and_drop(a, b).perform()
        action_chains.move_to_element(a).click_and_hold().move_by_offset(280, 150).release().perform()
