from src.the_internet.pages.entry_ad_page import EntryAd


def test_modal_shows_after_the_page_loads(driver, cfg):
    entry_ad = EntryAd(driver, cfg.base_url)

    entry_ad.get_entry_ad_page()
    assert entry_ad.modal_is_visible()


def test_modal_ui(driver, cfg):
    entry_ad = EntryAd(driver, cfg.base_url)

    entry_ad.get_entry_ad_page()


def test_modal_close(driver, cfg):
    entry_ad = EntryAd(driver, cfg.base_url)

    entry_ad.get_entry_ad_page()
    assert entry_ad.modal_is_visible()

    entry_ad.close_modal()
    assert not entry_ad.modal_is_visible(wait_time=2)
