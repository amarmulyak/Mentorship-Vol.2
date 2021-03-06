from http import HTTPStatus

from src.the_cat_api.image_params_data import SizeParam
from src.the_cat_api.images import Images
from src.utils.api import get_request_url
from src.utils.utils import cfg


def test_images_search_response_code():
    default_limit = 1
    image = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    response = image.get_images().json
    assert len(response) == default_limit


def test_images_search_limit():
    limit = 5
    image = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    response = image.get_images(size=SizeParam.FULL, limit=limit).json
    assert len(response) == limit


def test_download_url():
    image = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    url = image.get_images().get_response_item('$[0].url')
    get_url_response = get_request_url(url)
    assert get_url_response.status_code == HTTPStatus.OK
