import logging

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


class CustomResponse(Response):
    def __init__(self, response):
        super().__init__()
        self.response = response

    def status_code_is(self, status_code: int) -> 'CustomResponse':
        assert self.response.status_code == status_code

        return self

    def response_json(self):
        return self.response.json()

