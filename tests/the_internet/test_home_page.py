from src.the_internet.pages.home_page import HomePage
from src.the_internet.pages.ab_testing_page import ABTestingPage


def test_home_page_title(driver, cfg):
    home_page = HomePage(driver, cfg.base_url)
    home_page.get_home_page()
    assert home_page.home_page_title() == "Welcome to the-internet"


def test_ab_testing_link(driver, cfg):
    home_page = HomePage(driver, cfg.base_url)
    abtest_page = ABTestingPage(driver, cfg.base_url)
    home_page.get_home_page()
    home_page.click_ab_testing_link()
    assert abtest_page.abtest_page_reached()
