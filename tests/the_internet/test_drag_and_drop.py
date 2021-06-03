from src.the_internet.pages.drag_and_drop_page import DragAndDropPage


def test_drag_and_drop_a_to_b(driver, cfg):
    # GIVEN the Drag and Drop page is opened
    #   AND the element A is placed from the left
    drag_and_drop = DragAndDropPage(driver, cfg.base_url)
    drag_and_drop.get_drag_and_drop_page()
    assert drag_and_drop.column_a_text() == "A"

    # WHEN the element A dragged and dropped on the element B
    drag_and_drop.drag_and_drop_column_a_to_b()

    # THEN the element A is placed from the right
    assert drag_and_drop.column_b_text() == "A"


def test_drag_and_drop_b_to_a(driver, cfg):
    # GIVEN the Drag and Drop page is opened
    #   AND the element B is placed from the right
    drag_and_drop = DragAndDropPage(driver, cfg.base_url)
    drag_and_drop.get_drag_and_drop_page()
    assert drag_and_drop.column_b_text() == "B"

    # WHEN the element B dragged and dropped on the element A
    drag_and_drop.drag_and_drop_column_b_to_a()

    # THEN the element B is placed from the left
    assert drag_and_drop.column_a_text() == "B"
