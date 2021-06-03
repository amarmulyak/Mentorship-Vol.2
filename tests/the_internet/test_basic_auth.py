from src.the_internet.pages.basic_auth_page import BasicAuthPage


def test_basic_auth_valid_creds(driver, cfg):
    basic_auth = BasicAuthPage(driver, cfg.base_url)
    basic_auth.get_basic_auth_page(username="admin", password="admin")
    assert basic_auth.basic_auth_page_reached()
    assert basic_auth.basic_auth_title_text() == "Basic Auth"


def test_basic_auth_invalid_creds(driver, cfg):
    basic_auth = BasicAuthPage(driver, cfg.base_url)
    basic_auth.get_basic_auth_page(username="123", password="123")
    assert not basic_auth.basic_auth_page_reached(wait_time=2)
