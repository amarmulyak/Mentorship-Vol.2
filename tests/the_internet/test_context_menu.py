from src.the_internet.pages.context_menu_page import ContextMenuPage
from src.the_internet.pages.alert import Alert


def test_aller_appears_on_mouse_right_click(driver):
    context_menu = ContextMenuPage(driver)
    alert = Alert(driver)
    context_menu.get_context_menu_page()
    context_menu.right_mouse_click_on_box()
    assert alert.alert_is_present()


def test_alert_text(driver):
    context_menu = ContextMenuPage(driver)
    alert = Alert(driver)
    context_menu.get_context_menu_page()
    context_menu.right_mouse_click_on_box()
    alert.alert_text_equal("You selected a context menu")


def test_alert_accept(driver):
    context_menu = ContextMenuPage(driver)
    alert = Alert(driver)
    context_menu.get_context_menu_page()
    context_menu.right_mouse_click_on_box()
    alert.alert_accept()
    assert not alert.alert_is_present(wait_time=2)
