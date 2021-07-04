"""
File Uploader page module.
"""
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.the_internet.pages.base_page import BasePage


class FileUploaderPage(BasePage):
    """
    Class to represent File Uploader page.
    """

    CHOOSE_FILE_BTN = (By.ID, "file-upload")
    UPLOAD_BTN = (By.ID, "file-submit")
    DRAG_DROP_UPLOAD = (By.ID, "drag-drop-upload")
    UPLOADED_MSG = (By.TAG_NAME, "h3")
    UPLOADED_FILE = (By.XPATH, "//div[@class='example']/div")
    UPLOADED_FILES_DRAG_DROP = (By.XPATH, "//div[@class='dz-filename']/span[text()]")
    UPLOADED_FILE_DRAG_DROP = (
        By.XPATH,
        "//div[@class='dz-filename']/span[text()='{}']",
    )

    def get_file_uploader_page(self) -> None:
        """
        Open File Uploader page.

        :return: None
        """

        self.driver.get(f"{self.url}/upload")

    def choose_file_via_btn(self, file_path: str) -> None:
        """
        Upload file via upload button.

        :param file_path: Absolute path to file
        :return: None
        """

        choose = self.find_element(self.CHOOSE_FILE_BTN)
        choose.send_keys(file_path)

    def click_upload_btn(self) -> None:
        """
        Click the "Upload" button.

        :return: None
        """

        self.click_on_element(self.UPLOAD_BTN)

    def get_success_msg_text(self) -> str:
        """
        Get text from the success message.

        :return: Text
        """

        return self.get_element_text(self.UPLOADED_MSG)

    def get_uploaded_file_name(self) -> str:
        """
        Get uploaded file name.

        :return: File name
        """

        return self.get_element_text(self.UPLOADED_FILE)

    def drop_files_via_drag_and_drop(self, files: str) -> None:
        """
        Upload file via drag and drop.

        :param files: Single file path or list of file paths
        :return: None
        """

        drag_drop = self.find_element(self.DRAG_DROP_UPLOAD)
        self._drop_files(element=drag_drop, files=files)

    def get_list_of_uploaded_files_drag_drop(self) -> List[WebElement]:
        """
        Get list of elements of uploaded files.

        :return: List of WebElements
        """

        return self.driver.find_elements(*self.UPLOADED_FILES_DRAG_DROP)

    def is_file_uploaded_drag_drop(self, file_name: str) -> bool:
        """
        Check if file uploaded via Drag and Drop.

        :param file_name: Uploaded file name
        :return: True or False
        """

        return self.element_is_present(
            (
                self.UPLOADED_FILE_DRAG_DROP[0],
                self.UPLOADED_FILE_DRAG_DROP[1].format(file_name),
            )
        )
