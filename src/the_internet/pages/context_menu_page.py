from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from src.the_internet.pages.base_page import BasePage


class ContextMenuPage(BasePage):
    box_locator = (By.ID, "hot-spot")

    def get_context_menu_page(self):
        return self.driver.get("https://the-internet.herokuapp.com/context_menu")

    def right_mouse_click_on_box(self):
        box = self.find_element(self.box_locator)
        action = ActionChains(self.driver)
        return action.context_click(box).perform()
