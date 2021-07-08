"""
Base conftest module.
"""

import os
import pathlib
from datetime import datetime
from typing import Dict

import allure
import aumbry
import pytest
import yaml
from selenium import webdriver

from models.config import Config


@pytest.fixture(scope="session")
def get_base_path() -> pathlib.PosixPath:
    """
    Get the root folder path of the project.

    :return: PosixPath
    """

    return pathlib.Path(__file__).parent.parent


@pytest.fixture
def get_upload_dir_path(get_base_path):
    """
    Get the path with file to upload

    :param get_base_path: Fixture
    :return: Path
    """

    return f"{get_base_path}/src/the_internet/resource"


@pytest.fixture
def driver(cfg, download_dir, get_base_path):

    if cfg.browser.lower() == "firefox":
        driver = webdriver.Firefox(executable_path=f"{get_base_path}/drivers/geckodriver")
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
            executable_path=f"{get_base_path}/drivers/chromedriver", options=options
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


@pytest.fixture(scope="session")
def cfg(get_base_path) -> Config:
    """
    Get config as an object

    :param get_base_path: Fixture
    :return: Config object
    """

    cfg = aumbry.load(
        aumbry.FILE, Config, {"CONFIG_FILE_PATH": f"{get_base_path}/cfg/cfg.yaml"}
    )
    return cfg


@pytest.fixture(scope="session")
def cfg_as_dict(get_base_path) -> Dict:
    """
    Get config as dictionary

    :param get_base_path: Fixture
    :return: Config dict
    """

    with open(f"{get_base_path}/cfg/cfg.yaml") as f:
        cfg = yaml.load(f)
    return cfg


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
