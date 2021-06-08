from src.the_internet.pages.file_uploader_page import FileUploaderPage


def test_upload_via_button(driver, cfg):
    file_uploader = FileUploaderPage(driver, cfg.base_url)
    file_name = "box.png"

    file_uploader.get_file_uploader_page()
    file_uploader.choose_file_via_btn(f"src/the_internet/pages/{file_name}")
    file_uploader.click_upload_btn()
    assert file_uploader.success_msg() == "File Uploaded!"
    assert file_uploader.upladed_file_name() == file_name


def test_upload_drag_and_drop(driver, cfg):
    file_uploader = FileUploaderPage(driver, cfg.base_url)
    # file_name = "box.png"

    file_uploader.get_file_uploader_page()
    dd = file_uploader.find_element(file_uploader.DRAG_DROP_UPLOAD)
    file_uploader.drop_files(dd, '/home/amarm/repositories/Mentorship-Vol.2/src/the_internet/pages/box.png')
    abc = 1
