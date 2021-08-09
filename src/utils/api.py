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

    def get_response_attribute(self, attribute):
        json = self.response_json()

        if type(json) == list:
            return json[0].get(attribute)

        return json.get(attribute)

    def validate_json_schema(self, schema):
        return jsonschema.validate(self.response_json, schema)


m_d = {'a': 1, 'b': "hello"}

schema_v = {
    'type': 'object',
    'properties': {'a': {'type': 'number'},
                   'b': {'type': 'string'}}
}

jsonschema.validate(m_d, schema_v)

m_d_2 = [{'a': 1, 'b': "hello"}, {'a': '2', 'b': 'hello2'}]

schema_v_2 = {
    'type': 'array',
    'items': {'type': 'object',
              'properties': {'a': {'type': 'number'},
                             'b': {'type': 'string'}}
              }
    }

jsonschema.validate(m_d_2, schema_v_2)
