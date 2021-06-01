from src.the_internet.pages.dynamic_controls_page import DynamicControlsPage


def test_checkbox(driver):
    dynamic_controls = DynamicControlsPage(driver)
    dynamic_controls.get_dynamic_controls_page()
    assert dynamic_controls.checkbox_is_present()
    assert dynamic_controls.add_remove_button_caption_equal("Remove")

    dynamic_controls.click_add_remove_button()
    assert not dynamic_controls.checkbox_is_present(wait_time=2)
    assert dynamic_controls.checkbox_message_equal("It's gone!")

    dynamic_controls.click_add_remove_button()
    assert dynamic_controls.checkbox_is_present()
    assert dynamic_controls.checkbox_message_equal("It's back!")


def test_edit_field(driver):
    dynamic_controls = DynamicControlsPage(driver)

    dynamic_controls.get_dynamic_controls_page()
    assert dynamic_controls.input_field_is_disabled()
    assert dynamic_controls.enable_disable_button_caption_equal("Enable")

    dynamic_controls.click_enable_disable_button()
    assert not dynamic_controls.input_field_is_disabled()
    assert dynamic_controls.enable_disable_button_caption_equal("Disable")
    assert dynamic_controls.input_message_equal("It's enabled!")

    dynamic_controls.click_enable_disable_button()
    assert dynamic_controls.input_field_is_disabled()
    assert dynamic_controls.enable_disable_button_caption_equal("Enable")
    assert dynamic_controls.input_message_equal("It's disabled!")
