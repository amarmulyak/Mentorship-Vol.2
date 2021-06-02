from src.the_internet.pages.dynamically_loaded_elements_page1 import DynamicallyLoadedElementsPage1


def test_dynamically_loaded_elements(driver):
    page = DynamicallyLoadedElementsPage1(driver)

    page.get_dynamically_loaded_elements_page1()
    assert page.start_button_is_displayed()
    assert not page.dynamic_text_is_displayed()

    page.click_start_button()
    assert not page.start_button_is_displayed()
    assert page.dynamic_text_is_displayed()


def test_elements_text(driver):
    page = DynamicallyLoadedElementsPage1(driver)

    page.get_dynamically_loaded_elements_page1()

    assert page.dynamic_text_is_displayed()
    # assert page.start_button_caption_equal("Start")
    # assert page.dynamic_text_equal("Hello World!")
