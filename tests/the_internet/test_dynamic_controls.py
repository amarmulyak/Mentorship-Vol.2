from src.the_internet.pages.dynamic_controls_page import DynamicControlsPage


def test_checkbox(driver):
    dynamic_controls = DynamicControlsPage(driver)
    dynamic_controls.get_dynamic_controls_page()
    assert dynamic_controls.is_checkbox_present()
    assert dynamic_controls.add_remove_button_caption() == "Remove"

    dynamic_controls.click_add_remove_button()
    assert not dynamic_controls.is_checkbox_present(wait_time=2)
    assert dynamic_controls.checkbox_message_text() == "It's gone!"

    dynamic_controls.click_add_remove_button()
    assert dynamic_controls.is_checkbox_present()
    assert dynamic_controls.checkbox_message_text() == "It's back!"


def test_edit_field(driver):
    dynamic_controls = DynamicControlsPage(driver)

    dynamic_controls.get_dynamic_controls_page()
    assert dynamic_controls.is_input_field_disabled()
    assert dynamic_controls.enable_disable_button_caption() == "Enable"

    dynamic_controls.click_enable_disable_button()
    assert not dynamic_controls.is_input_field_disabled()
    assert dynamic_controls.enable_disable_button_caption() == "Disable"
    assert dynamic_controls.input_message_text() == "It's enabled!"

    dynamic_controls.click_enable_disable_button()
    assert dynamic_controls.is_input_field_disabled()
    assert dynamic_controls.enable_disable_button_caption() == "Enable"
    assert dynamic_controls.input_message_text() == "It's disabled!"


