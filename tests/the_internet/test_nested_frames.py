from src.the_internet.pages.nested_frames import NestedFramesPage


def test_frames_text(driver):
    page = NestedFramesPage(driver)

    page.get_nested_frames_page()
    page.switch_to_left_frame()
    assert page.get_frame_text() == "LEFT"

    page.switch_to_middle_frame()
    assert page.get_frame_text() == "MIDDLE"

    page.switch_to_right_frame()
    assert page.get_frame_text() == "RIGHT"

    page.switch_to_bottom_frame()
    assert page.get_frame_text() == "BOTTOM"
