from selenium import webdriver
import pathlib
import pytest


@pytest.fixture
def driver():
    cur_path = pathlib.Path(__file__).parent.parent
    driver = webdriver.Chrome(executable_path=f"{cur_path}/drivers/chromedriver")
    yield driver
    driver.quit()
