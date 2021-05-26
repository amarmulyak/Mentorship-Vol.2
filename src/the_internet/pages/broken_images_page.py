from src.the_internet.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import requests


class BrokenImagesPage(BasePage):
    images_locator = (By.TAG_NAME, "img")

    def get_add_broken_images_page(self):
        return self.driver.get(self.base_url + "broken_images")

    def check_for_broken_images(self):
        # TODO Зробити гет брокен імеджес і гет не брокен імеджес
        images = self.find_elements(self.images_locator)
        for image in images:
            response = requests.get(image.get_attribute("src"))
            assert response.status_code == 200
