from src.the_internet.pages.entry_ad_page import EntryAd


def test_modal_appears_after_the_first_page_load(driver, cfg):
    entry_ad = EntryAd(driver, cfg.base_url)

    entry_ad.get_entry_ad_page()
    assert entry_ad.is_modal_visible()


def test_modal_ui(driver, cfg):
    entry_ad = EntryAd(driver, cfg.base_url)

    entry_ad.get_entry_ad_page()
    assert entry_ad.get_modal_title_text() == "THIS IS A MODAL WINDOW"
    assert (
        entry_ad.get_modal_body_text()
        == "It's commonly used to encourage a user to take an "
        "action (e.g., give their e-mail address to sign up"
        " for something or disable their ad blocker)."
    )


def test_modal_close(driver, cfg):
    entry_ad = EntryAd(driver, cfg.base_url)

    entry_ad.get_entry_ad_page()
    assert entry_ad.is_modal_visible()

    entry_ad.close_modal()
    assert not entry_ad.is_modal_visible(wait_time=2)


def test_modal_doesnt_appear_on_subsequent_loads(driver, cfg):
    entry_ad = EntryAd(driver, cfg.base_url)

    entry_ad.get_entry_ad_page()
    assert entry_ad.is_modal_visible()

    entry_ad.close_modal()
    assert not entry_ad.is_modal_visible(wait_time=2)

    driver.refresh()
    assert not entry_ad.is_modal_visible(wait_time=2)


def test_modal_appears_after_re_enabling(driver, cfg):
    entry_ad = EntryAd(driver, cfg.base_url)

    entry_ad.get_entry_ad_page()
    assert entry_ad.is_modal_visible()

    entry_ad.close_modal()
    assert not entry_ad.is_modal_visible(wait_time=2)

    driver.refresh()
    assert not entry_ad.is_modal_visible(wait_time=2)

    entry_ad.click_restart_add()
    driver.refresh()
    assert entry_ad.is_modal_visible()
