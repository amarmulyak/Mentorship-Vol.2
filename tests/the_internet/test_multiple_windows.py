from src.the_internet.pages.multiple_windows import MultipleWindow


def test_multiple_window(driver, cfg):
    page = MultipleWindow(driver, cfg.base_url)

    page.get_multiple_window_page()

    window_before = driver.current_window_handle
    page.click_on_click_here_button()

    open_windows = driver.window_handles
    new_window = [window for window in open_windows if window != window_before][0]
    driver.switch_to_window(new_window)
    driver.close()
    driver.switch_to_window(window_before)
