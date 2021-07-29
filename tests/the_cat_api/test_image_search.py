from typing import Dict

from src.the_cat_api.image_params_data import SizeParam
from src.the_cat_api.images import Images


def test_image_search():
    images = Images()
    r = images.get_images_search(size=SizeParam.FULL.value, mime_types=True)
    assert r.status_code == 200

    r_dict = images.get_response_as_dict(r)
    assert isinstance(r_dict, Dict)
    assert len(r_dict) > 0
