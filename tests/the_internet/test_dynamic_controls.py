from src.the_internet.pages.dynamic_controls_page import DynamicControlsPage
import time


def test_checkbox(driver):
    dynamic_controls = DynamicControlsPage(driver)
    dynamic_controls.get_dynamic_controls_page()

    dynamic_controls.verify_checkbox_present(True)
    dynamic_controls.check_add_remove_button_caption("Remove")
    dynamic_controls.click_add_remove_button()
    # Need advice here as I wait 10 extra seconds to find the element
    dynamic_controls.verify_checkbox_present(False)
    assert dynamic_controls.message_has_text("It's gone!")

    dynamic_controls.click_add_remove_button()
    dynamic_controls.verify_checkbox_present(True)
    assert dynamic_controls.message_has_text("It's back!")


def test_edit_field(driver):
    dynamic_controls = DynamicControlsPage(driver)
    dynamic_controls.get_dynamic_controls_page()

    dynamic_controls.check_edit_field_enabled()