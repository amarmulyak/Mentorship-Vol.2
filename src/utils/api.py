import logging
from typing import List

import requests
from requests import Response

logger = logging.getLogger()


def parse_response(response: Response) -> List:
    """
    Get response as Python Object

    :param response: Response
    :return: List of dicts
    """

    logger.info(f'Parsing response {response.text}')

    return response.json()


def get_url(url: str) -> Response:
    """
    Get URL

    :param url: URL
    :return: Response
    """

    return requests.get(url)
