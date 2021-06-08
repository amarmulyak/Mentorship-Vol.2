from src.the_internet.pages.file_downloader_page import FileDownloaderPage


def test_download_files(driver, cfg, download_dir):
    file_downloader = FileDownloaderPage(driver, cfg.base_url, download_dir)

    file_downloader.get_file_downloader_page()
    file_downloader.download_files()
    files = file_downloader.list_of_files()
    for file in files:
        assert file_downloader.file_exists(file)
