"""
Images Params Data module
"""

import requests
import logging

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

    def get_images_search(self, limit: int = None, size: SizeParam = None):
        """
        Get request for image search

        :param limit: Limit of images
        :param size: Image size
        :return: List of images
        """

        logger.info(f'GET images search request (params: limit={limit}, size={size})')

        params = {}

        if limit:
            params['limit'] = limit
        if size:
            params['size'] = size

        return requests.get(self.endpoint, headers={"x-api-key": self.x_api_key}, params=params)
