"""
Module to represent Images endpoint
"""

import logging

import requests
from requests import Response

from src.the_cat_api.image_params_data import SizeParam
from http import HTTPStatus

logger = logging.getLogger()


class Images:
    """
    Class to represent Images endpoint
    """

    PATH = "images/search"

    def __init__(self, endpoint: str, x_api_key: str):
        self.endpoint = f'{endpoint}/{self.PATH}'
        self.x_api_key = x_api_key

    def get_images(self, limit: int = None, size: SizeParam = None) -> Response:
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

        response = requests.get(self.endpoint,
                                headers={"x-api-key": self.x_api_key},
                                params=params)

        logger.debug(f'Request: GET {self.endpoint} |'
                     f' Params: limit={limit}, size={size})'
                     f' | Status Code: {response.status_code} | Response: {response.text}')

        assert response.status_code == HTTPStatus.OK

        return response
