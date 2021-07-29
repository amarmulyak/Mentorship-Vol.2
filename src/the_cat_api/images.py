"""
Images Params Data module
"""

import json

import requests

from src.the_cat_api.image_params_data import SizeParam
from src.utils.utils import cfg


class Images:
    """
    Images Class
    """
    def __init__(self):
        self.endpoint = f"{cfg().the_cat_api.url}/images/search"

    def get_images_search(self, size: SizeParam = None, mime_types: bool = None):
        """
        Get request for image search

        :param size: request param (Enum)
        :param mime_types: request param
        :return: Request response
        """

        params = {}

        if size:
            params['size'] = size
        if mime_types:
            params['mime_types'] = True

        return requests.get(self.endpoint, headers={"x-api-key": f"{cfg().the_cat_api.x_api_key}"}, params=params)

    @staticmethod
    def get_response_as_dict(response):
        """
        Get response text as dict

        :param response: Response text
        :return: Response dict
        """

        return json.loads(response.text)
