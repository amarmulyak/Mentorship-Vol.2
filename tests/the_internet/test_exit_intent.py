from src.the_internet.pages.exit_intent_page import ExitIntent


def test_modal_doesnt_appear_on_page_load(driver, cfg):
    page = ExitIntent(driver, cfg.base_url)
    page.get_exit_intent_page()

    assert not page.is_modal_visible(wait_time=2)


def test_modal_appear_when_mouse_out(driver, cfg):
    page = ExitIntent(driver, cfg.base_url)

    page.get_exit_intent_page()
    assert not page.is_modal_visible(wait_time=2)

    page.move_mouse_out_of_viewport()
    assert page.is_modal_visible()
