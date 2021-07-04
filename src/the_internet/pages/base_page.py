"""
BasePage module.
"""

import os
from typing import List, Tuple

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop

from src.utils.drop_file_js import JS_DROP_FILES


class BasePage:
    """
    A Class to represent base methods.
    """

    _PAGE_TITLE = (By.XPATH, "//div[@class='example']/h3")

    def __init__(self, driver: webdriver, url: str) -> None:
        """
        :param driver: webdriver
        :param url: URL of the site
        """

        self.driver = driver
        self.url = url

    def find_element(self, locator: Tuple[By, str], time: int = 10) -> WebElement:
        """
        Find element.

        :param locator: Locator
        :param time: Time
        :return: WebElement
        """

        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_elements(self, locator: Tuple[By, str], time: int = 10) -> List[WebElement]:
        """
        Find elements.

        :param locator: Locator
        :param time: Time
        :return: List of WebElements
        """

        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    def wait_until_visible(self, locator: Tuple[By, str], time: int = 10) -> WebElement:
        """
        Wait until element will be visible.

        :param locator: Locator
        :param time: Time
        :return: WebElement
        """

        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Locator {locator} is not visible",
        )

    def wait_until_invisible(self, locator: Tuple[By, str], time=10):
        """
        Wait until element will be invisible.

        :param locator: Locator
        :param time: Time
        :return: WebElement
        """

        return WebDriverWait(self.driver, time).until(
            EC.invisibility_of_element(locator),
            message=f"Locator {locator} is not visible",
        )

    def wait_until_text_in_element(self, locator: Tuple[By, str], text, time=10):
        """
        Wait until text in element.

        :param locator: Locator
        :param text: Text expected in WebElement
        :param time: Time
        :return: WebElement
        """

        return WebDriverWait(self.driver, time).until(
            EC.text_to_be_present_in_element(locator, text),
            message=f"Locator {locator} is not visible",
        )

    def wait_until_element_clickable(self, locator: Tuple[By, str], time=10):
        """
        Wait until element will be clickable.

        :param locator: Locator
        :param time: Time
        :return: WebElement
        """

        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message=f"Locator {locator} is not clickable",
        )

    def click_on_element(self, locator: Tuple[By, str]):
        """
        Click on element.

        :param locator: Locator
        :return: None
        """

        return self.find_element(locator).click()

    def get_element_text(self, locator: Tuple[By, str]) -> str:
        """
        Get element text.

        :param locator: Locator
        :return: Element text
        """

        return self.find_element(locator).text

    def element_is_present(self, locator: Tuple[By, str], wait_time=10):
        """
        Check if element present.

        :param locator: Locator
        :param wait_time: Time
        :return: True or False
        """

        try:
            self.find_element(locator, time=wait_time)
            element_found = True
        except TimeoutException:
            element_found = False
        return element_found

    def element_is_visible(self, locator: Tuple[By, str], wait_time=10):
        """
        Check if element visible.

        :param locator: Locator
        :param wait_time: Time
        :return: True or False
        """

        try:
            self.wait_until_visible(locator, time=wait_time)
            element_visible = True
        except TimeoutException:
            element_visible = False
        return element_visible

    def provide_text_to_element(self, locator: Tuple[By, str], text):
        """
        Provide text to element.

        :param locator: Locator
        :param text: Text you want to provide
        :return: None
        """

        self.find_element(locator).send_keys(text)

    def _drop_files(self, element: WebElement, files: str):
        """
        Upload file via drag and drop.

        :param element: Drag and drop element
        :param files: Single file path or list of file paths
        :return: None
        """

        offset_x = 0
        offset_y = 0
        # TODO зробити джава скріпт окремим файлом
        js_drop_files = JS_DROP_FILES

        paths = []

        for file in files if isinstance(files, List) else [files]:
            if not os.path.isfile(file):
                raise FileNotFoundError(file)
            paths.append(file)

        value = "\n".join(paths)
        elm_input = self.driver.execute_script(
            js_drop_files, element, offset_x, offset_y
        )
        elm_input._execute("sendKeysToElement", {"value": [value], "text": value})

    def _drag_and_drop(self, source_locator: Tuple[By, str], target_locator: Tuple[By, str]):
        """
        Drag and drop element from the source to the target locator.

        :param source_locator: Locator of the source element
        :param target_locator: Locator of the target element
        :return: None
        """

        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        drag_and_drop(self.driver, source, target)
