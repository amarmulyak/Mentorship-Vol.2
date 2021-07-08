"""
Dynamic Controls page module.
"""

from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class DynamicControlsPage(BasePage):
    """
    Class to represent Dynamic Controls page.
    """

    _CHECKBOX = (By.ID, "checkbox")
    _CHECKBOX_ADD_REMOVE_BUTTON = (By.XPATH, "//form[@id='checkbox-example']/button")
    _CHECKBOX_LOADER = (By.XPATH, "//form[@id='checkbox-example']/div[@id='loading']")
    _CHECKBOX_MESSAGE = (By.XPATH, "//form[@id='checkbox-example']/p[@id='message']")
    _INPUT_LOADER = (By.XPATH, "//form[@id='input-example']/div[@id='loading']")
    _INPUT_FIELD = (By.XPATH, "//input[@type='text']")
    _INPUT_ENABLE_DISABLE_BTN = (By.XPATH, "//form[@id='input-example']/button")
    _INPUT_MESSAGE = (By.XPATH, "//form[@id='input-example']/p[@id='message']")

    def get_dynamic_controls_page(self) -> None:
        """
        Open Dynamic Controls page.

        :return: None
        """

        return self.driver.get(f"{self.url}/dynamic_controls")

    def is_checkbox_present(self, wait_time=10) -> bool:
        """
        Check if checkbox is present.

        :param wait_time: Time to wait the element (default is 10)
        :return: True or False
        """

        return self.element_is_present(self._CHECKBOX, wait_time)

    def click_add_remove_button(self) -> None:
        """
        Click on the Add/Remove button.

        :return: None
        """

        self.click_on_element(self._CHECKBOX_ADD_REMOVE_BUTTON)
        self.wait_until_invisible(self._CHECKBOX_LOADER)

    def checkbox_message_text(self) -> str:
        """
        Get checkbox message text.

        :return: Text of the message
        """

        return self.get_element_text(self._CHECKBOX_MESSAGE)

    def add_remove_button_caption(self) -> str:
        """
        Get text of the Add/Remove button caption.

        :return: Text of the button caption
        """

        return self.get_element_text(self._CHECKBOX_ADD_REMOVE_BUTTON)

    def is_input_field_disabled(self) -> bool:
        """
        Check if input field is disabled.

        :return: True or False
        """

        edit_field = self.find_element(self._INPUT_FIELD)
        return bool(edit_field.get_attribute("disabled"))

    def enable_disable_button_caption(self) -> str:
        """
        Get text of the Enable/Disable button caption.

        :return: Text of the button caption
        """

        return self.get_element_text(self._INPUT_ENABLE_DISABLE_BTN)

    def click_enable_disable_button(self) -> None:
        """
        Click on the Enable/Disable button.

        :return: None
        """

        self.click_on_element(self._INPUT_ENABLE_DISABLE_BTN)
        self.wait_until_invisible(self._INPUT_LOADER)

    def input_message_text(self) -> str:
        """
        Get input's message text.

        :return: Text of the message
        """

        return self.get_element_text(self._INPUT_MESSAGE)
