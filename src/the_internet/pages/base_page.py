"""
BasePage module.
"""

import os
from typing import List
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from src.utils.drop_file_js import JS_DROP_FILES


class BasePage:
    """
    A Class to represent base methods .
    """

    _PAGE_TITLE = (By.XPATH, "//div[@class='example']/h3")

    def __init__(self, driver, url):
        """
        :param driver: webdriver
        :param url: URL of the site
        """

        self.driver = driver
        self.url = url

    def find_element(self, locator, time=10):
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

    def find_elements(self, locator, time=10):
        """
        Find elements.

        :param locator: Locator
        :param time: Time
        :return: WebElements
        """

        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    def wait_until_visible(self, locator, time=10):
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

    def wait_until_invisible(self, locator, time=10):
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

    def wait_until_text_in_element(self, locator, text, time=10):
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

    def wait_until_element_clickable(self, locator, time=10):
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

    def click_on_element(self, locator):
        """
        Click on element.

        :param locator: Locator
        :return: None
        """

        return self.find_element(locator).click()

    def get_element_text(self, locator):
        """
        Get element text.

        :param locator: Locator
        :return: Element text
        """

        return self.find_element(locator).text

    def element_is_present(self, locator, wait_time=10):
        """
        Check if element present

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

    def element_is_visible(self, locator, wait_time=10):
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

    def provide_text_to_element(self, locator, text):
        """
        Provide text to element

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
        # TODO Оксана: ревю чи ок так тримати джава скріпт
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
