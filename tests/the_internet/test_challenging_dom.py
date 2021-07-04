from src.the_internet.pages.challenging_dom_page import ChallengingDomPage


def test_get_answer(driver, cfg):
    challenging_dom = ChallengingDomPage(driver, cfg.base_url)
    challenging_dom.get_challenging_dom_page()
    challenging_dom.get_answer()  # Can't get canvas.strokeText


def test_cell_data(driver, cfg):
    challenging_dom = ChallengingDomPage(driver, cfg.base_url)
    challenging_dom.get_challenging_dom_page()
    cell_data1 = challenging_dom.get_data_from_cell(1, "Lorem")
    assert cell_data1 == "Iuvaret0"
    cell_data2 = challenging_dom.get_data_from_cell(2, "Ipsum")
    assert cell_data2 == "Apeirian1"
    cell_data3 = challenging_dom.get_data_from_cell(3, "Dolor")
    assert cell_data3 == "Adipisci2"
