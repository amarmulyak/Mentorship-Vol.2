"""
Base conftest module.
"""

import logging
import os
import pathlib
from datetime import datetime

import allure
import pytest
from selenium import webdriver

from src.utils.utils import get_base_path, cfg

cfg_ = cfg()
base_path = get_base_path()


@pytest.fixture
def get_upload_dir_path():
    """
    Get the path with file to upload

    :return: Path
    """

    return f"{base_path}/src/the_internet/resource"


@pytest.fixture
def driver(download_dir):
    if cfg_.browser.lower() == "firefox":
        driver = webdriver.Firefox(executable_path=f"{base_path}/drivers/geckodriver")
        driver.maximize_window()
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")

        prefs = {
            "profile.default_content_settings.popups": 0,
            "download.prompt_for_download": "false",
            "download.default_directory": download_dir,
            "safebrowsing.enabled": True,
        }
        options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(
            executable_path=f"{base_path}/drivers/chromedriver", options=options
        )
    yield driver
    driver.quit()


@pytest.fixture
def download_dir(tmpdir_factory) -> str:
    """
    Create temporary download directory.

    :param tmpdir_factory: Builtin fixture
    :return: Download directory path
    """

    _dir = tmpdir_factory.mktemp("download")
    return _dir.strpath


def pytest_configure(config) -> None:
    """
    Add folder to take Allure report results

    :param config: Builtin fixture
    :return: None
    """

    allure_folder = pathlib.Path(__file__).parent / "allure_result_folder"
    allure_folder.mkdir(exist_ok=True)
    for item in allure_folder.iterdir():
        if item.is_file():
            item.unlink()
    config.option.allure_report_dir = allure_folder

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-8s - %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    fh_1 = logging.FileHandler("log_1.log", mode='w')
    fh_1.setLevel(logging.INFO)
    fh_1.setFormatter(formatter)
    fh_2 = logging.FileHandler("log_2.log", mode='w')
    fh_2.setLevel(logging.ERROR)
    fh_2.setFormatter(formatter)
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    ch.setLevel(logging.INFO)
    logger.addHandler(fh_1)
    logger.addHandler(fh_2)
    logger.addHandler(ch)


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item) -> None:
    """
    When the test fails, take a screenshot automatically and display
    it in the allure report.

    :param item: Builtin fixture
    :return: None
    """

    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            allure_folder = pathlib.Path(__file__).parent / "allure_result_folder"
            now_time = datetime.now().strftime("%Y%m%d%H%M%S")
            screen_path = os.path.join(allure_folder, "{}.png".format(now_time))
            feature_request = item.funcargs['request']
            driver = feature_request.getfixturevalue("driver")
            driver.save_screenshot(screen_path)
            allure.attach.file(screen_path, now_time, allure.attachment_type.PNG)
