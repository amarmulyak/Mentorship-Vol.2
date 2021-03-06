from src.the_internet.pages.multiple_windows import MultipleWindows


def test_multiple_window(driver):
    page = MultipleWindows(driver)

    page.get_multiple_window_page()
    page.click_on_click_here_link()
    assert page.count_open_windows() == 2

    page.switch_to_next_window()
    assert page.get_page_title() == "New Window"

    page.switch_to_previous_window()
    assert page.get_page_title() == "Opening a new window"
