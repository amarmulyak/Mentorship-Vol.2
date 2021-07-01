"""
File Downloader module.
"""

from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class FileDownloaderPage(BasePage):
    """
    Class to represent File Downloader page.
    """

    DOWNLOAD_LINKS = (By.XPATH, '//div[@class="example"]/a[@href]')
    DOWNLOAD_LINK = (By.XPATH, '//div[@class="example"]/a[text()="{}"]')

    def __init__(self, driver, url, download_dir_path):
        """
        :param driver: webdriver
        :param url: URL of the site
        :param download_dir_path: Path to download files
        """

        super().__init__(driver, url)
        self.download_dir_path = download_dir_path

    def get_file_downloader_page(self):
        """
        Open File Downloader page.

        :return:
        """

        self.driver.get(f"{self.url}/download")

    def _get_list_of_download_links_elements(self):
        """
        Get list of links to download files.

        :return: List of WebElements
        """

        return self.find_elements(self.DOWNLOAD_LINKS)

    def download_file(self, file_name):
        f"""
        Click on "file_name" name link.
        
        :param file_name: Name of the file which is present in the link
        :return: None
        """

        self.click_on_element(
            (self.DOWNLOAD_LINK[0], self.DOWNLOAD_LINK[1].format(file_name))
        )

    def get_list_of_file_names(self):
        """
        Get list of file names.

        :return: List of file names taken from the download links
        """

        return [
            el.get_attribute("text")
            for el in self._get_list_of_download_links_elements()
        ]
