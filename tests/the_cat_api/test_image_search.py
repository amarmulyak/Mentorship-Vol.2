from src.the_cat_api.images import Images
import json


def test_get_vote():
    images = Images()
    r = images.get_images_search(size="full")
    r_dict = json.loads(r.content)
    a = 1

