from src.the_internet.pages.file_downloader_page import FileDownloaderPage
from src.utils.utils import file_exists


def test_download_files(driver, cfg, download_dir):
    file_downloader = FileDownloaderPage(driver, cfg.base_url, download_dir)

    file_downloader.get_file_downloader_page()
    files = file_downloader.get_list_of_file_names()
    for file in files:
        if file.endswith((".jar", ".py")):
            continue
        file_downloader.download_file(file)
        assert file_exists(f"{download_dir}/{file}")


# TODO Налаштувати браузер для скачування файлів .py .jar
