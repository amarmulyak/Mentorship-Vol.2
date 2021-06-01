from src.the_internet.pages.dynamically_loaded_elements_page1 import DynamicallyLoadedElementsPage1


def test_dynamically_loaded_elements(driver):
    page = DynamicallyLoadedElementsPage1(driver)

    page.get_dynamically_loaded_elements_page1()
    assert page.start_button_is_displayed()
    assert not page.dynamic_text_is_displayed()
