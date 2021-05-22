from src.the_internet.pages.basic_auth_page import BasicAuthPage


def test_basic_auth_valid_creds(driver):
    basic_auth = BasicAuthPage(driver)
    basic_auth.get_basic_auth_page(username="admin", password="admin")
    basic_auth.check_basic_auth_title()


def test_basic_auth_invalid_creds(driver):
    basic_auth = BasicAuthPage(driver)
    basic_auth.get_basic_auth_page(username="123", password="123")
    basic_auth.check_basic_auth_title()
