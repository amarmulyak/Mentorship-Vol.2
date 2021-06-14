from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class JavaScriptAlertsPage(BasePage):
    JS_ALLERT = (By.XPATH, "//button[contains(text(), 'Click for JS Alert')]")
    JS_CONFIRM = (By.XPATH, "//button[contains(text(), 'Click for JS Confirm')]")
    JS_PROMPT = (By.XPATH, "//button[contains(text(), 'Click for JS Prompt')]")
    RESULT = (By.ID, "result")

    def get_javascript_alerts_page(self):
        self.driver.get(f"{self.url}/javascript_alerts")

    def click_js_alert_button(self):
        self.click_on_element(self.JS_ALLERT)

    def click_js_confirm_button(self):
        self.click_on_element(self.JS_CONFIRM)

    def click_js_prompt_button(self):
        self.click_on_element(self.JS_PROMPT)

    def get_result(self):
        return self.get_element_text(self.RESULT)
