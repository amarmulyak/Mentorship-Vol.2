from typing import Dict

from src.the_cat_api.image_params_data import SizeParam
from src.the_cat_api.images import Images
from src.utils.utils import cfg
from src.utils.api import parse_response
from http import HTTPStatus


def test_image_search_response_code():
    image = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    response = image.get_images_search()
    assert response.status_code == HTTPStatus.OK


def test_image_search_limit():
    limit = 5
    image = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    response = image.get_images_search(size=SizeParam.FULL.value, limit=limit)
    parsed_response = parse_response(response)
    assert len(parsed_response) == limit
