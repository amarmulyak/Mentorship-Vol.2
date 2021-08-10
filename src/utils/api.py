import logging

import requests
from requests import Response

import jsonschema

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


class CustomResponse(Response):
    def __init__(self, response):
        super().__init__()
        self._response = response

    def status_code_is(self, status_code: int) -> 'CustomResponse':
        assert self._response.status_code == status_code

        return self

    def response_json(self):
        return self._response.json()

    def get_response_attribute(self, attribute):
        json = self.response_json()

        if type(json) == list:
            return json[0].get(attribute)

        return json.get(attribute)

    def validate_json_schema(self, schema):
        jsonschema.validate(self._response.json(), schema)
