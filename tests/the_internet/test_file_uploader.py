from src.the_internet.pages.file_uploader_page import FileUploaderPage


# TODO винести файл в папку resource + генерити свій файл
def test_upload_via_button(driver, cfg):
    file_uploader = FileUploaderPage(driver, cfg.base_url)
    file_name = "box.png"

    file_uploader.get_file_uploader_page()
    file_uploader.choose_file_via_btn(f"src/the_internet/pages/{file_name}")
    file_uploader.click_upload_btn()
    assert file_uploader.success_msg() == "File Uploaded!"
    assert file_uploader.upladed_file_name() == file_name


def test_upload_file_via_drag_and_drop(driver, cfg):
    file_uploader = FileUploaderPage(driver, cfg.base_url)
    file_name = "box.png"

    file_uploader.get_file_uploader_page()
    file_uploader.drop_file_via_drag_and_drop(f"src/the_internet/pages/{file_name}")
    assert len(file_uploader.get_list_of_uploaded_files_drag_drop()) == 1
