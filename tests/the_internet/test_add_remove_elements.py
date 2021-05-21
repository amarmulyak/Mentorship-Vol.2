import time
from src.the_internet.pages.add_remove_elements_page import AddRemoveElementsPage


def test_add_element(driver):
    add_remove_elements = AddRemoveElementsPage(driver)
    add_remove_elements.get_add_remove_elements_page()
    add_remove_elements.add_element()
    time.sleep(5)
