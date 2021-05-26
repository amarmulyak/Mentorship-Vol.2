from src.the_internet.pages.home_page import HomePage
from src.the_internet.pages.ab_testing_page import ABTestingPage
import pytest


def test_home_page_title(driver):
    home_page = HomePage(driver)
    home_page.get_home_page()
    assert home_page.home_page_title_has_text("Welcome to the-internet")


@pytest.mark.flaky(reruns=5)
def test_ab_testing_link(driver):
    home_page = HomePage(driver)
    abtest_page = ABTestingPage(driver)
    home_page.get_home_page()
    home_page.click_on_element(home_page.ab_testing_link_locator)
    abtest_page.abtest_page_title_has_text()
