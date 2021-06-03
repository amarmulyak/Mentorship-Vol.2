from src.the_internet.pages.context_menu_page import ContextMenuPage
from src.the_internet.pages.alert import Alert


def test_aller_appears_on_mouse_right_click(driver, cfg):
    context_menu = ContextMenuPage(driver, cfg.base_url)
    alert = Alert(driver)
    context_menu.get_context_menu_page()
    context_menu.right_mouse_click_on_box()
    assert alert.is_present()


def test_alert_text(driver, cfg):
    context_menu = ContextMenuPage(driver, cfg.base_url)
    alert = Alert(driver)
    context_menu.get_context_menu_page()
    context_menu.right_mouse_click_on_box()
    alert.text_equal("You selected a context menu")


def test_alert_accept(driver, cfg):
    context_menu = ContextMenuPage(driver, cfg.base_url)
    alert = Alert(driver)
    context_menu.get_context_menu_page()
    context_menu.right_mouse_click_on_box()
    alert.accept()
    assert not alert.is_present(wait_time=2)
