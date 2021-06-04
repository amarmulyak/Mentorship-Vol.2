from src.the_internet.pages.entry_ad_page import EntryAd


def test_modal_ui(driver, cfg):
    entry_ad = EntryAd(driver, cfg.base_url)
