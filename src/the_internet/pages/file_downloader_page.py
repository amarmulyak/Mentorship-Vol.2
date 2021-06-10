from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class FileDownloaderPage(BasePage):
    DOWNLOAD_LINKS = (By.XPATH, '//div[@class="example"]/a[@href]')
    DOWNLOAD_LINK = (By.XPATH, '//div[@class="example"]/a[text()="{}"]')

    def __init__(self, driver, url, download_dir_path):
        super().__init__(driver, url)
        self.download_dir_path = download_dir_path

    def get_file_downloader_page(self):
        self.driver.get(f"{self.url}/download")

    def _get_list_of_download_links_elements(self):
        return self.find_elements(self.DOWNLOAD_LINKS)

    def download_file(self, file_name):
        self.click_on_element((
            self.DOWNLOAD_LINK[0],
            self.DOWNLOAD_LINK[1].format(file_name)
        ))

    def get_list_of_file_names(self):
        return [el.get_attribute("text") for el in self._get_list_of_download_links_elements()]

