from src.the_cat_api.image_params_data import SizeParam
from src.the_cat_api.images import Images
from src.utils.utils import cfg
from src.utils.api import parse_response, get_url, get_response_attribute_type
from http import HTTPStatus


def test_images_search_response_code():
    image = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    response = image.get_images()
    assert response.status_code == HTTPStatus.OK


def test_images_search_limit():
    limit = 5
    image = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    response = image.get_images(size=SizeParam.FULL.value, limit=limit)
    parsed_response = parse_response(response)
    assert len(parsed_response) == limit


def test_images_search_response():
    image = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    response = parse_response(image.get_images())[0]

    assert get_response_attribute_type(response['breeds']) == list
    assert get_response_attribute_type(response['id']) == str
    assert get_response_attribute_type(response['url']) == str
    assert get_response_attribute_type(response['width']) == int
    assert get_response_attribute_type(response['height']) == int


def test_download_url():
    image = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key)
    response = parse_response(image.get_images())[0]
    get_url_response = get_url(response['url'])
    assert get_url_response.status_code == HTTPStatus.OK
