from selenium import webdriver
import pathlib
import pytest


@pytest.fixture
def driver():
    cur_path = pathlib.Path(__file__).parent.parent
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        executable_path=f"{cur_path}/drivers/chromedriver", chrome_options=options
    )
    yield driver
    driver.quit()
