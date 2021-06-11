from src.the_internet.pages.multiple_windows import MultipleWindow


def test_multiple_window(driver, cfg):
    page = MultipleWindow(driver, cfg.base_url)

    page.get_multiple_window_page()
