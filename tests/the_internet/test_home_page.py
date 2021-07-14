from src.the_internet.pages.home_page import HomePage
from src.the_internet.pages.ab_testing_page import ABTestingPage


def test_home_page_title(driver):
    home_page = HomePage(driver)
    home_page.get_home_page()
    assert home_page.get_home_page_title_text() == "Welcome to the-internet"


def test_ab_testing_link(driver):
    home_page = HomePage(driver)
    abtest_page = ABTestingPage(driver)
    home_page.get_home_page()
    home_page.click_ab_testing_link()
    assert abtest_page.abtest_page_reached()


def test_dynamic_loading_link(driver):
    home_page = HomePage(driver)

    home_page.get_home_page()
    dynamic_elements = home_page.click_dynamic_loading_link()
    assert dynamic_elements.is_page_reached()

    example1 = dynamic_elements.click_example_1_link()
    assert example1.is_page_reached()

    driver.back()
    example2 = dynamic_elements.click_example_2_link()
    assert example2.is_page_reached()
