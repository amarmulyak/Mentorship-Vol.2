from src.the_internet.pages.broken_images_page import BrokenImagesPage
import pytest


@pytest.mark.xfail(reason="Two broken images currently present")
def test_broken_images(driver):
    broken_images = BrokenImagesPage(driver)
    broken_images.get_add_broken_images_page()
    not_broken_images, broken_images = broken_images.get_images()
    assert not_broken_images
    assert not broken_images
