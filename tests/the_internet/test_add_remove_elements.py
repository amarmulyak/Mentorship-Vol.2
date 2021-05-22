from src.the_internet.pages.add_remove_elements_page import AddRemoveElementsPage


def test_add_element(driver):
    add_remove_elements = AddRemoveElementsPage(driver)
    add_remove_elements.get_add_remove_elements_page()
    add_remove_elements.add_element()
    add_remove_elements.check_buttons_quantity(1)


def test_add_elements(driver):
    add_remove_elements = AddRemoveElementsPage(driver)
    add_remove_elements.get_add_remove_elements_page()
    add_remove_elements.add_elements(5)
    add_remove_elements.check_buttons_quantity(5)


def test_delete_element(driver):
    add_remove_elements = AddRemoveElementsPage(driver)
    add_remove_elements.get_add_remove_elements_page()
    add_remove_elements.add_elements(1)
    add_remove_elements.check_buttons_quantity(1)
    add_remove_elements.delete_button(1)
    add_remove_elements.check_buttons_quantity(0, time=2)


def test_delete_random_elements(driver):
    add_remove_elements = AddRemoveElementsPage(driver)
    add_remove_elements.get_add_remove_elements_page()
    add_remove_elements.add_elements(5)
    add_remove_elements.check_buttons_quantity(5)
    add_remove_elements.delete_button(5)
    add_remove_elements.delete_button(3)
    add_remove_elements.check_buttons_quantity(3)


def test_delete_all_elements(driver):
    add_remove_elements = AddRemoveElementsPage(driver)
    add_remove_elements.get_add_remove_elements_page()
    add_remove_elements.add_elements(5)
    add_remove_elements.check_buttons_quantity(5)
    add_remove_elements.delete_buttons()
    add_remove_elements.check_buttons_quantity(0, time=2)
