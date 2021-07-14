from src.the_internet.pages.shadow_dom_page import ShadowDomPage


def test_shadow_dom(driver):
    page = ShadowDomPage(driver)

    page.get_shadow_dom_page()
    assert page.get_section1_text() == "Let's have some different text!"
    assert page.get_section2_row1_text() == "Let's have some different text!"
    assert page.get_section2_row2_text() == "In a list!"
