from src.the_internet.pages.dynamically_loaded_elements_page1 import DynamicallyLoadedElementsPage1


def test_dynamically_loaded_elements(driver, cfg):
    page = DynamicallyLoadedElementsPage1(driver, cfg.base_url)

    page.get_dynamically_loaded_elements_page1()
    assert page.start_button_is_visible()
    assert not page.dynamic_text_is_visible(wait_time=2)

    page.click_start_button()
    assert not page.start_button_is_visible(wait_time=2)
    assert page.dynamic_text_is_visible()


def test_elements_text(driver, cfg):
    page = DynamicallyLoadedElementsPage1(driver, cfg.base_url)

    page.get_dynamically_loaded_elements_page1()
    assert page.start_button_caption() == "Start"

    page.click_start_button()
    assert page.dynamic_text() == "Hello World!"
