from selenium import webdriver
import pathlib
import pytest
import yaml
import aumbry
from models.config import Config

cur_path = pathlib.Path(__file__).parent.parent


@pytest.fixture
def driver(cfg):
    if cfg.browser.lower() == "firefox":
        driver = webdriver.Firefox(executable_path=f"{cur_path}/drivers/geckodriver")
        driver.maximize_window()
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(
            executable_path=f"{cur_path}/drivers/chromedriver", options=options
        )
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def cfg():
    cfg = aumbry.load(aumbry.FILE, Config, {'CONFIG_FILE_PATH': f'{cur_path}/cfg/cfg.yaml'})
    return cfg


@pytest.fixture(scope="session")
def cfg_as_dict():
    with open(f"{cur_path}/cfg/cfg.yaml") as f:
        cfg = yaml.load(f)
    return cfg
