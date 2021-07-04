"""
Java Script Alerts page module.
"""

from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class JavaScriptAlertsPage(BasePage):
    """
    Class to represent Java Script Alert page.
    """

    JS_ALLERT = (By.XPATH, "//button[contains(text(), 'Click for JS Alert')]")
    JS_CONFIRM = (By.XPATH, "//button[contains(text(), 'Click for JS Confirm')]")
    JS_PROMPT = (By.XPATH, "//button[contains(text(), 'Click for JS Prompt')]")
    RESULT = (By.ID, "result")

    def get_javascript_alerts_page(self) -> None:
        """
        Open Java Script Alert page.

        :return: None
        """

        self.driver.get(f"{self.url}/javascript_alerts")

    def click_js_alert_button(self) -> None:
        """
        Click "JS Alert" button.

        :return: None
        """

        self.click_on_element(self.JS_ALLERT)

    def click_js_confirm_button(self) -> None:
        """
        Click "JS Confirm" button.

        :return: None
        """

        self.click_on_element(self.JS_CONFIRM)

    def click_js_prompt_button(self) -> None:
        """
        Click "JS Prompt" button.

        :return: None
        """

        self.click_on_element(self.JS_PROMPT)

    def get_result(self) -> str:
        """
        Get result text.

        :return: Text
        """

        return self.get_element_text(self.RESULT)
