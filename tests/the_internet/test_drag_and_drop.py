from src.the_internet.pages.drag_and_drop_page import DragAndDropPage
import time


def test_drag_and_drop_a_to_b(driver):
    # GIVEN the Drag and Drop page is opened
    #   AND the element A is placed from the left
    drag_and_drop = DragAndDropPage(driver)
    drag_and_drop.get_drag_and_drop_page()
    assert drag_and_drop.element_text_equal(drag_and_drop.element_a_locator, "A")

    # WHEN the element A dragged and dropped on the element B
    drag_and_drop.drag_and_drop(
        drag_and_drop.element_a_locator,
        drag_and_drop.element_b_locator
    )

    # THEN the element A is placed from the right
    assert drag_and_drop.element_text_equal(drag_and_drop.element_b_locator, "A")


def test_drag_and_drop_b_to_a(driver):
    # GIVEN the Drag and Drop page is opened
    #   AND the element B is placed from the right
    drag_and_drop = DragAndDropPage(driver)
    drag_and_drop.get_drag_and_drop_page()
    assert drag_and_drop.element_text_equal(drag_and_drop.element_b_locator, "B")

    # WHEN the element B dragged and dropped on the element A
    drag_and_drop.drag_and_drop(
        drag_and_drop.element_b_locator,
        drag_and_drop.element_a_locator
    )

    # THEN the element B is placed from the left
    assert drag_and_drop.element_text_equal(drag_and_drop.element_a_locator, "B")

