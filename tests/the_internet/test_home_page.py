from src.the_internet.pages.home_page import HomePage
from src.the_internet.pages.ab_testing_page import ABTestingPage


def test_home_page_title(driver):
    home_page = HomePage(driver)
    home_page.get_home_page()
    assert home_page.home_page_title_equal("Welcome to the-internet")


def test_ab_testing_link(driver):
    home_page = HomePage(driver)
    abtest_page = ABTestingPage(driver)
    home_page.get_home_page()
    home_page.click_ab_testing_link()
    assert abtest_page.abtest_page_reached()
