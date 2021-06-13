from src.the_internet.pages.multiple_windows import MultipleWindow


def test_multiple_window(driver, cfg):
    page = MultipleWindow(driver, cfg.base_url)

    page.get_multiple_window_page()
    window_before = driver.current_window_handle
    page.click_on_click_here_button()
    assert len(driver.window_handles) == 2

    new_window = driver.window_handles[1]
    driver.switch_to_window(new_window)
    assert page.get_page_title() == "New Window"

    driver.close()
    driver.switch_to_window(window_before)
    assert page.get_page_title() == "Opening a new window"
    assert len(driver.window_handles) == 1
