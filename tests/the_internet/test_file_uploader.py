from src.the_internet.pages.file_uploader_page import FileUploaderPage


def test_upload_via_button(driver, cfg, base_path):
    file_uploader = FileUploaderPage(driver, cfg.base_url)

    file_uploader.get_file_uploader_page()
    file_uploader.choose_file_via_btn(
        f"{base_path}/src/the_internet/resource/box.png")
    file_uploader.click_upload_btn()
    assert file_uploader.success_msg() == "File Uploaded!"
    assert file_uploader.upladed_file_name() == "box.png"


def test_upload_generated_file_via_button(driver, cfg, base_path, tmpdir):
    file_uploader = FileUploaderPage(driver, cfg.base_url)
    file = tmpdir.join('test.txt')
    file.write("Test")

    file_uploader.get_file_uploader_page()

    file_uploader.choose_file_via_btn(file.strpath)
    file_uploader.click_upload_btn()
    assert file_uploader.success_msg() == "File Uploaded!"
    assert file_uploader.upladed_file_name() == "test.txt"


def test_upload_file_via_drag_and_drop(driver, cfg, base_path, tmpdir):
    file_uploader = FileUploaderPage(driver, cfg.base_url)
    file = tmpdir.join('test.txt')
    file.write("Test")

    file_uploader.get_file_uploader_page()
    file_uploader.drop_files_via_drag_and_drop(
        f"{base_path}/src/the_internet/resource/box.png")
    assert len(file_uploader.get_list_of_uploaded_files_drag_drop()) == 1
    assert file_uploader.is_file_uploaded_drag_drop("box.png")

    file_uploader.drop_files_via_drag_and_drop(file.strpath)
    assert len(file_uploader.get_list_of_uploaded_files_drag_drop()) == 2
    assert file_uploader.is_file_uploaded_drag_drop("test.txt")
