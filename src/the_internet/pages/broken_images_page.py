"""
Broken images module.
"""

import requests
from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class BrokenImagesPage(BasePage):
    """
    Class to represent Broken Images page.
    """

    _IMAGES = (By.TAG_NAME, "img")

    def get_add_broken_images_page(self):
        """
        Open Broken Images page.

        :return: None
        """

        return self.driver.get(f"{self.url}/broken_images")

    def get_correct_images(self):
        """
        Get list of images on the page which are not broken.

        :return: List of not broken images
        """

        images = self.driver.find_elements(*self._IMAGES)
        correct_images_list = []
        if images:
            for image in images:
                response = requests.get(image.get_attribute("src"))
                if response.status_code == 200:
                    correct_images_list.append(image)
        return correct_images_list

    def get_broken_images(self):
        """
        Get list of images on the page which are broken.

        :return: List of broken images
        """

        images = self.driver.find_elements(*self._IMAGES)
        broken_images_list = []
        if images:
            for image in images:
                response = requests.get(image.get_attribute("src"))
                if response.status_code != 200:
                    broken_images_list.append(image)
        return broken_images_list
