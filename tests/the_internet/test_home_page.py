from src.the_internet.pages.home_page import HomePage
from src.the_internet.pages.ab_testing_page import ABTestingPage
import pytest


def test_home_page_title(driver):
    home_page = HomePage(driver)
    home_page.get_home_page()
    home_page.check_home_page_title()


@pytest.mark.flaky(reruns=5)
def test_ab_testing_link(driver):
    home_page = HomePage(driver)
    abtest_page = ABTestingPage(driver)
    home_page.get_home_page()
    home_page.click_on_element(home_page.ab_testing_link)
    abtest_page.check_abtest_page_title()
