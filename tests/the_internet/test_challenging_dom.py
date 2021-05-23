from src.the_internet.pages.challenging_dom_page import ChallengingDomPage


def test_get_answer(driver):
    challenging_dom = ChallengingDomPage(driver)
    challenging_dom.get_challenging_dom_page()
    challenging_dom.get_answer()  # Can't get canvas.strokeText
