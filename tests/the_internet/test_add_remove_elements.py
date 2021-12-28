from src.the_internet.pages.add_remove_elements_page import AddRemoveElementsPage


def test_add_element(driver):
    add_remove_elements = AddRemoveElementsPage(driver)
    add_remove_elements.get_add_remove_elements_page()
    add_remove_elements.add_element()
    # assert len(add_remove_elements.get_delete_buttons()) == 1
    assert len(add_remove_elements.get_delete_buttons()) == 1


def test_add_elements(driver):
    add_remove_elements = AddRemoveElementsPage(driver)
    add_remove_elements.get_add_remove_elements_page()
    add_remove_elements.add_elements(5)
    assert len(add_remove_elements.get_delete_buttons()) == 5


def test_delete_element(driver):
    add_remove_elements = AddRemoveElementsPage(driver)
    add_remove_elements.get_add_remove_elements_page()
    add_remove_elements.add_elements(1)
    assert len(add_remove_elements.get_delete_buttons()) == 1
    add_remove_elements.delete_button(button_index=0)
    assert len(add_remove_elements.get_delete_buttons()) == 0


def test_delete_random_elements(driver):
    add_remove_elements = AddRemoveElementsPage(driver)
    add_remove_elements.get_add_remove_elements_page()
    add_remove_elements.add_elements(5)
    assert len(add_remove_elements.get_delete_buttons()) == 5
    add_remove_elements.delete_button(button_index=4)
    add_remove_elements.delete_button(button_index=2)
    assert len(add_remove_elements.get_delete_buttons()) == 3


def test_delete_all_elements(driver):
    add_remove_elements = AddRemoveElementsPage(driver)
    add_remove_elements.get_add_remove_elements_page()
    add_remove_elements.add_elements(5)
    assert len(add_remove_elements.get_delete_buttons()) == 5
    add_remove_elements.delete_buttons()
    assert len(add_remove_elements.get_delete_buttons()) == 0
