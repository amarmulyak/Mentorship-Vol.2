from src.the_cat_api.images import Images


def test_get_vote():
    images = Images()
    r = images.get_images_search()
    a = 1
