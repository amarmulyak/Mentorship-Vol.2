from src.the_internet.pages.drag_and_drop_page import DragAndDropPage
import time


def test_drag_and_drop(driver):
    drag_and_drop = DragAndDropPage(driver)
    drag_and_drop.get_drag_and_drop_page()
    drag_and_drop.drag_and_drop_column_a_to_b()
    time.sleep(5)
