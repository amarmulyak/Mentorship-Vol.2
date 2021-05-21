from src.the_internet.pages.home_page import HomePage
from src.the_internet.pages.a_b_testing_page import ABTestingPage


def test_home_page_title(driver):
    home_page = HomePage(driver)
    home_page.get_home_page()
    home_page.check_home_page_title()


def test_a_b_testing_link(driver):
    home_page = HomePage(driver)
    abtest_page = ABTestingPage(driver)
    home_page.get_home_page()
    home_page.click_on_element(home_page.a_b_testing_link)
    abtest_page.check_abtest_page_title()
