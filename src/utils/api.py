import logging
from typing import List

from requests import Response

logger = logging.getLogger()


def parse_response(response: Response) -> List:
    """
    Get response as dict

    :param response: Response
    :return: List of dicts
    """

    logger.info(f'Parsing response {response.text}')

    return response.json()
