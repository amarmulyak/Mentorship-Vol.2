from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class ContextMenuPage(BasePage):
    # box_locator = (By.ID, "hot-spot")
    box_locator = (By.XPATH, "//div[@id='hot-spot']")

    def get_context_menu_page(self):
        return self.driver.get(self.base_url + "context_menu")

    def right_mouse_click_on_box(self):
        box = self.find_element(self.box_locator)
        action = ActionChains(self.driver)
        return action.context_click(box).perform()

