from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoAlertPresentException


class ContextMenuPage(BasePage):
    box_locator = (By.ID, "hot-spot")

    def get_context_menu_page(self):
        return self.driver.get(self.base_url + "context_menu")

    def right_mouse_click_on_box(self):
        box = self.find_element(self.box_locator)
        action = ActionChains(self.driver)
        return action.context_click(box).perform()

    def check_alert_appear(self):
        # TODO Додати свій клас для роботи з алертом
        self.wait_until_alert_appear()
        popup = self.driver.switch_to.alert
        assert popup.text == "You selected a context menu"

    def check_alert_disappears_on_ok(self):
        popup = self.driver.switch_to.alert
        popup.accept()
        self.wait_until_alert_disappear()
        try:
            self.driver.switch_to.alert
            alert_not_shown = False
        except NoAlertPresentException:
            alert_not_shown = True
        assert alert_not_shown
