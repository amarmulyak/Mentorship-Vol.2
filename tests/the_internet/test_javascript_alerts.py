import pytest
from src.the_internet.pages.java_script_alerts_page import JavaScriptAlertsPage
from src.the_internet.pages.alert import Alert


def test_js_alert(driver, cfg):
    page = JavaScriptAlertsPage(driver, cfg.base_url)
    alert = Alert(driver)

    page.get_javascript_alerts_page()
    page.click_js_alert_button()
    alert.accept()
    assert page.get_result() == "You successfully clicked an alert"


def test_js_confirm(driver, cfg):
    page = JavaScriptAlertsPage(driver, cfg.base_url)
    alert = Alert(driver)

    page.get_javascript_alerts_page()
    page.click_js_confirm_button()
    alert.accept()
    assert page.get_result() == "You clicked: Ok"

    page.click_js_confirm_button()
    alert.dismiss()
    assert page.get_result() == "You clicked: Cancel"


text_data = ("Hello1", "123456789", '!@#$%^&*()_+{}:"|<>?[];\./\'-`~')


@pytest.mark.parametrize("text", text_data)
def test_js_prompt(driver, cfg, text):
    page = JavaScriptAlertsPage(driver, cfg.base_url)
    alert = Alert(driver)

    page.get_javascript_alerts_page()
    page.click_js_prompt_button()
    alert.send_keys(text)
    alert.accept()
    assert page.get_result() == f"You entered: {text}"

    page.click_js_prompt_button()
    alert.send_keys(text)
    alert.dismiss()
    assert page.get_result() == "You entered: null"
