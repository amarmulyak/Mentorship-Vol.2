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


def test_dynamic_loading_link(driver, cfg):
    home_page = HomePage(driver, cfg.base_url)

    home_page.get_home_page()
    dynamic_elements = home_page.click_dynamic_loading_link()
    assert dynamic_elements.page_is_reached()

    example1 = dynamic_elements.click_example_1_link()
    assert example1.page_is_reached()

    driver.back()
    example2 = dynamic_elements.click_example_2_link()
    assert example2.page_is_reached()
