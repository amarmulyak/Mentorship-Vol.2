from src.the_internet.pages.dynamic_controls_page import DynamicControlsPage
import time


def test_checkbox(driver):
    dynamic_controls = DynamicControlsPage(driver)
    dynamic_controls.get_dynamic_controls_page()

    assert dynamic_controls.checkbox_is_present()
    assert dynamic_controls.add_remove_button_has_caption("Remove")
    dynamic_controls.click_add_remove_button()
    # Need advice here as I wait 10 extra seconds to find the element
    assert not dynamic_controls.checkbox_is_present()
    assert dynamic_controls.message_has_text("It's gone!")

    dynamic_controls.click_add_remove_button()
    assert dynamic_controls.checkbox_is_present()
    assert dynamic_controls.message_has_text("It's back!")


def test_edit_field(driver):
    dynamic_controls = DynamicControlsPage(driver)
    dynamic_controls.get_dynamic_controls_page()

    assert dynamic_controls.edit_field_is_disabled()
