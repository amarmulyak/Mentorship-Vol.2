from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage


class FileUploaderPage(BasePage):
    CHOOSE_FILE_BTN = (By.ID, "file-upload")
    UPLOAD_BTN = (By.ID, "file-submit")
    DRAG_DROP_UPLOAD = (By.ID, "drag-drop-upload")
    UPLOADED_MSG = (By.TAG_NAME, "h3")
    UPLOADED_FILE = (By.XPATH, "//div[@class='example']/div")
    UPLADED_FILES_DRAG_DROP = (By.XPATH, "//div[@id='drag-drop-upload']//span[contains(text(), 'png')]")

    def get_file_uploader_page(self):
        self.driver.get(f"{self.url}/upload")

    def choose_file_via_btn(self, file_path):
        choose = self.find_element(self.CHOOSE_FILE_BTN)
        choose.send_keys(file_path)

    def click_upload_btn(self):
        self.click_on_element(self.UPLOAD_BTN)

    def success_msg(self):
        return self.element_text(self.UPLOADED_MSG)

    def upladed_file_name(self):
        return self.element_text(self.UPLOADED_FILE)

    def drop_files_via_drag_and_drop(self, files: str):
        """
        Upload file via drag and drop
        :param files: Single file path or list of file paths
        :return: None
        """
        drag_drop = self.find_element(self.DRAG_DROP_UPLOAD)
        self._drop_files(element=drag_drop, files=files)

    def get_list_of_uploaded_files_drag_drop(self):
        return self.driver.find_elements(*self.UPLADED_FILES_DRAG_DROP)
