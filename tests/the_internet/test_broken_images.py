from src.the_internet.pages.broken_images_page import BrokenImagesPage


def test_broken_images(driver):
    broken_images = BrokenImagesPage(driver)
    broken_images.get_add_broken_images_page()
    broken_images.check_for_broken_images()
