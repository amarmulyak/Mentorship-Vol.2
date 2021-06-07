from src.the_internet.pages.file_downloader_page import FileDownloaderPage


def test_download_flower_jpeg(driver, cfg, download_dir):
    file_downloader = FileDownloaderPage(driver, cfg.base_url)

    file_downloader.get_file_downloader_page()
    file_downloader.click_flower_jpeg_link()
    assert file_downloader.flower_jpeg_downloaded(download_dir)


def test_nmax_py(driver, cfg, download_dir):
    file_downloader = FileDownloaderPage(driver, cfg.base_url)

    file_downloader.get_file_downloader_page()
    file_downloader.click_test_nmax_py_link()
    assert file_downloader.test_nmax_py_downloaded(download_dir)
