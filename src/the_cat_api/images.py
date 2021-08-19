"""
Module to represent Images endpoint
"""

import logging
from http import HTTPStatus

import requests

from src.the_cat_api.image_params_data import SizeParam
from src.the_cat_api.schema import GET_IMAGES_SCHEMA
from src.utils.api import CustomResponseV2

logger = logging.getLogger()


class Images:
    """
    Class to represent Images endpoint
    """

    PATH = "images/search"

    def __init__(self, endpoint: str, x_api_key: str):
        self.endpoint = f'{endpoint}/{self.PATH}'
        self.x_api_key = x_api_key

    def get_images(self, limit: int = None, size: SizeParam = None) -> CustomResponseV2:
        """
        Get request for image search

        :param limit: Limit of images
        :param size: Image size
        :return: Response (list of images)
        """

        params = {}

        if limit:
            params['limit'] = limit
        if size:
            params['size'] = size.value

        response = CustomResponseV2(requests.get(self.endpoint,
                                                 headers={"x-api-key": self.x_api_key},
                                                 params=params))

        logger.debug(f'Request: GET {self.endpoint} |'
                     f' Params: limit={limit}, size={size})'
                     f' | Status Code: {response.status_code} | Response: {response.text}')

        response.status_code_is(HTTPStatus.OK)

        response.validate_json_schema(GET_IMAGES_SCHEMA)

        return response
