from src.the_internet.pages.context_menu_page import ContextMenuPage


def test_get_answer(driver):
    context_menu = ContextMenuPage(driver)
    context_menu.get_context_menu_page()
    context_menu.right_mouse_click_on_box()
    context_menu.check_alert_appear()
    context_menu.check_alert_disappears_on_ok()
