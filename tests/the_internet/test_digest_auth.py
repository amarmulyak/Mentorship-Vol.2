from src.the_internet.pages.digest_auth_page import DigestAuthPage


def test_basic_auth_valid_creds(driver, cfg):
    digest_auth = DigestAuthPage(driver, cfg.base_url)
    digest_auth.get_basic_auth_page(username="admin", password="admin")
    assert digest_auth.digest_auth_page_reached()
    assert digest_auth.digest_auth_title_text() == "Digest Auth"


def test_basic_auth_invalid_creds(driver, cfg):
    digest_auth = DigestAuthPage(driver, cfg.base_url)
    digest_auth.get_basic_auth_page(username="123", password="123")
    assert not digest_auth.digest_auth_page_reached(wait_time=2)
