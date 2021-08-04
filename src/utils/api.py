import logging
from typing import List

import requests
from requests import Response

logger = logging.getLogger()


def get_request_url(url: str) -> Response:
    """
    Get request URL

    :param url: URL
    :return: Response
    """

    return requests.get(url)


def get_response_attribute(response: Response, attr: str):
    response = response.json()
    return response.get(attr)


def get_response_attribute_type(attribute):
    return type(attribute)
