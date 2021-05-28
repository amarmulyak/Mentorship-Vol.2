from src.the_internet.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import requests


class BrokenImagesPage(BasePage):
    images_locator = (By.TAG_NAME, "img")

    def get_add_broken_images_page(self):
        return self.driver.get("https://the-internet.herokuapp.com/broken_images")

    def get_images(self):
        images = self.driver.find_elements(*self.images_locator)
        not_broken_images_list = []
        broken_images_list = []
        if images:
            for image in images:
                response = requests.get(image.get_attribute("src"))
                if response.status_code == 200:
                    not_broken_images_list.append(image)
                else:
                    broken_images_list.append(image)
        return not_broken_images_list, broken_images_list
