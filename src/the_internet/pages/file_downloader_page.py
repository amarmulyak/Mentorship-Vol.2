from selenium.webdriver.common.by import By
import pathlib
from src.the_internet.pages.base_page import BasePage
from PIL import Image
import time


class FileDownloaderPage(BasePage):
    DOWNLOAD_LINKS = (By.XPATH, "//div[@class='example']/a[@href]")

    def __init__(self, driver, url, download_dir_path):
        super().__init__(driver, url)
        self.download_dir_path = download_dir_path

    def get_file_downloader_page(self):
        self.driver.get(f"{self.url}/download")

    def list_of_links(self):
        return self.find_elements(self.DOWNLOAD_LINKS)

    def list_of_files(self):
        return [f"{self.download_dir_path}/{el.get_attribute('text')}" for el in self.list_of_links()]

    def download_files(self):
        for el in self.list_of_links():
            el.click()

    def file_exists(self, file_path):
        f = pathlib.Path(file_path)
        if not f.exists():  # Need to wait until file is downloading
            time.sleep(5)
        return f.exists()

    def _file_is_an_image(self, file_path):
        try:
            Image.open(file_path)
            file_is_image = True
        except IOError:
            file_is_image = False
        return file_is_image
