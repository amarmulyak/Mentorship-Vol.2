from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pathlib
import pytest
import yaml
import aumbry
from models.config import Config


@pytest.fixture(scope="session")
def base_path():
    return pathlib.Path(__file__).parent.parent


@pytest.fixture
def driver(cfg, download_dir, base_path):
    if cfg.browser.lower() == "firefox":
        driver = webdriver.Firefox(executable_path=f"{base_path}/drivers/geckodriver")
        driver.maximize_window()
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        # options.add_argument("--safebrowsing-disable-download-protection")
        # options.add_argument("safebrowsing-disable-extension-blacklist")

        prefs = {
            "profile.default_content_settings.popups": 0,
            "download.prompt_for_download": "false",
            "download.default_directory": download_dir,
            # "disable-popup-blocking": "true",
            # 'download.extensions_to_open': 'py',
            "safebrowsing.enabled": True,
        }
        options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(
            executable_path=f"{base_path}/drivers/chromedriver", options=options
        )
    yield driver
    driver.quit()

# @pytest.fixture
# def driver(cfg, download_dir, base_path):
#     if cfg.browser.lower() == "firefox":
#         driver = webdriver.Firefox(executable_path=f"{base_path}/drivers/geckodriver")
#         driver.maximize_window()
#     else:
#         chrome_options = Options()
#         chrome_options.add_argument("--disable-infobars")
#         chrome_options.add_argument("start-maximized")
#         chrome_options.add_argument("--disable-extensions")
#         chrome_options.add_argument("--disable-popup-blocking")
#         chrome_options.add_argument('--disable-gpu')
#         chrome_options.add_argument('--disable-software-rasterizer')
#         chrome_options.add_argument('--safebrowsing-disable-download-protection')
#
#         # disable the banner "Chrome is being controlled by automated test software"
#         chrome_options.add_experimental_option("useAutomationExtension", False)
#         chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
#
#         prefs = {
#             'download.default_directory': 'download_directory',
#             'download.prompt_for_download': False,
#             'download.extensions_to_open': 'jar',
#             'safebrowsing.enabled': True
#         }
#         capabilities = DesiredCapabilities().CHROME
#         chrome_options.add_experimental_option('prefs', prefs)
#         capabilities.update(chrome_options.to_capabilities())
#
#         driver = webdriver.Chrome(
#             executable_path=f"{base_path}/drivers/chromedriver", options=chrome_options
#         )
#     yield driver
#     driver.quit()


@pytest.fixture
def download_dir(tmpdir_factory):
    _dir = tmpdir_factory.mktemp('download')
    return _dir.strpath


@pytest.fixture(scope="session")
def cfg(base_path):
    cfg = aumbry.load(aumbry.FILE, Config, {'CONFIG_FILE_PATH': f'{base_path}/cfg/cfg.yaml'})
    return cfg


@pytest.fixture(scope="session")
def cfg_as_dict(base_path):
    with open(f"{base_path}/cfg/cfg.yaml") as f:
        cfg = yaml.load(f)
    return cfg
