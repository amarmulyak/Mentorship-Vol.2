from selenium.webdriver.common.by import By
import pathlib
from src.the_internet.pages.base_page import BasePage
from PIL import Image


class FileDownloaderPage(BasePage):
    FLOWER_JPEG = (By.LINK_TEXT, "flower.jpeg")
    TEST_NMAX_PY = (By.LINK_TEXT, "test_nmax.py")

    def __init__(self, driver, url, download_dir_path):
        super().__init__(driver, url)
        self.download_dir_path = download_dir_path

    def get_file_downloader_page(self):
        self.driver.get(f"{self.url}/download")

    def click_flower_jpeg_link(self):
        self.click_on_element(self.FLOWER_JPEG)

    def click_test_nmax_py_link(self):
        self.click_on_element(self.TEST_NMAX_PY)

    def _file_exists(self, file):
        f = pathlib.Path(file)
        return f.is_file()

    def _file_is_an_image(self, file):
        try:
            Image.open(file)
            file_is_image = True
        except IOError:
            file_is_image = False
        return file_is_image

    def _flower_jpeg_path(self):
        file = self.element_text(self.FLOWER_JPEG)
        return f"{self.download_dir_path}/{file}"

    def flower_jpeg_downloaded(self):
        return self._file_exists(self._flower_jpeg_path())

    def flower_jpeg_is_image(self):
        return self._file_is_an_image(self._flower_jpeg_path())

    def _test_nmax_py_path(self):
        file = self.element_text(self.TEST_NMAX_PY)
        return f"{self.download_dir_path}/{file}"

    def test_nmax_py_downloaded(self):
        return self._file_exists(self._test_nmax_py_path())

    def test_nmax_py_is_image(self):
        return self._file_is_an_image(self._test_nmax_py_path())
