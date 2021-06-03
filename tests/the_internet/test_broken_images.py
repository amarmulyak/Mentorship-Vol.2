from src.the_internet.pages.broken_images_page import BrokenImagesPage


def test_broken_images(driver, cfg):
    broken_images = BrokenImagesPage(driver, cfg.base_url)
    broken_images.get_add_broken_images_page()
    correct_images_list = broken_images.get_correct_images()
    broken_images_list = broken_images.get_broken_images()
    assert len(correct_images_list) == 2
    assert len(broken_images_list) == 2
