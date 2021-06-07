from selenium.webdriver.common.by import By
import pathlib
from src.the_internet.pages.base_page import BasePage


class FileDownloaderPage(BasePage):
    FLOWER_JPEG = (By.LINK_TEXT, "flower.jpeg")
    TEST_NMAX_PY = (By.LINK_TEXT, "test_nmax.py")

    def get_file_downloader_page(self):
        self.driver.get(f"{self.url}/download")

    def click_flower_jpeg_link(self):
        self.click_on_element(self.FLOWER_JPEG)

    def click_test_nmax_py_link(self):
        self.click_on_element(self.TEST_NMAX_PY)

    def file_exists(self, path, locator):
        file = self.element_text(locator)
        return pathlib.Path(f"{path}/{file}")

    def flower_jpeg_downloaded(self, path):
        return self.file_exists(path, self.FLOWER_JPEG)

    def test_nmax_py_downloaded(self, path):
        return self.file_exists(path, self.TEST_NMAX_PY)
