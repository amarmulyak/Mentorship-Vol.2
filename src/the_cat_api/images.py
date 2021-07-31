"""
Images Params Data module
"""

import logging

import requests
from requests import Response

from src.the_cat_api.image_params_data import SizeParam

logger = logging.getLogger()


class Images:
    """
    Images Class
    """

    PATH = "images/search"

    def __init__(self, endpoint, x_api_key):
        self.endpoint = f'{endpoint}/{self.PATH}'
        self.x_api_key = x_api_key

    def get_images(self, limit: int = None, size: SizeParam = None) -> Response:
        """
        Get request for image search

        :param limit: Limit of images
        :param size: Image size
        :return: List of images
        """

        params = {}

        if limit:
            params['limit'] = limit
        if size:
            params['size'] = size

        response = requests.get(self.endpoint,
                                headers={"x-api-key": self.x_api_key},
                                params=params)

        logger.info(f'GET images search request (params: limit={limit}, size={size})'
                    f' | Response: {response.json()}')

        return response
