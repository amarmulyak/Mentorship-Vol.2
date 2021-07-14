from src.the_internet.pages.dynamically_loaded_elements_page_e2 import DynamicallyLoadedElementsPageE2


def test_dynamically_loaded_elements(driver):
    page = DynamicallyLoadedElementsPageE2(driver)

    page.get_dynamically_loaded_elements_page2()
    assert page.is_start_button_visible()
    assert not page.is_dynamic_text_visible(wait_time=2)

    page.click_start_button()
    assert not page.is_start_button_visible(wait_time=2)
    assert page.is_dynamic_text_visible()


def test_elements_text(driver):
    page = DynamicallyLoadedElementsPageE2(driver)

    page.get_dynamically_loaded_elements_page2()
    assert page.get_start_button_caption() == "Start"

    page.click_start_button()
    assert page.get_dynamic_text() == "Hello World!"
