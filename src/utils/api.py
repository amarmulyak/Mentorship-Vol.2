"""
Module to represent API utils
"""

import logging
from typing import Any, List, Dict

import jsonschema
import requests
from requests import Response

from src.utils.utils import get_json_path

logger = logging.getLogger()


def get_request_url(url: str) -> Response:
    """
    Get request URL

    :param url: URL
    :return: Response
    """

    return requests.get(url)


class CustomResponse:
    """
    Class to represent the custom response
    """

    def __init__(self, response: requests.Response):
        super().__init__()
        self._response = response

    def status_code_is(self, status_code: int) -> 'CustomResponse':
        """
        Assert the response status code

        :param status_code: Expected status code
        :return: CustomResponse
        """

        assert self._response.status_code == status_code, f'Got {self._response.status_code} instead of {status_code}'

        return self

    @property
    def status_code(self) -> int:
        """
        Get the response status code

        :return: Status code
        """

        return self._response.status_code

    @property
    def text(self) -> str:
        """
        Get the response text

        :return: Response text
        """

        return self._response.text

    @property
    def json(self) -> Any:
        """
        Get the response json

        :return: Response json
        """

        return self._response.json()

    def get_response_attribute(self, attribute: Any) -> Any:
        """
        Get the specified attribute from the response

        :param attribute: Attribute to ge
        :return: Attribute value
        :raise: KeyError if the attribute is not found
        """

        json = self.json

        if isinstance(json, list):
            result = json[0].get(attribute)
        else:
            result = json.get(attribute)

        if result is None:
            raise KeyError(f'No {attribute!r} attribute in {json}')

        return result

    def validate_json_schema(self, schema: Dict) -> 'CustomResponse':
        """
        Validate response json schema

        :param schema: Specified schema as pattern
        :return: CustomResponse
        """

        jsonschema.validate(self._response.json(), schema)

        return self


class CustomResponseV2:
    """
    Class to represent the custom response v2 with alternative parse response methods
    """

    def __init__(self, response: requests.Response):
        super().__init__()
        self._response = response

    def status_code_is(self, status_code: int) -> 'CustomResponseV2':
        """
        Assert the response status code

        :param status_code: Expected status code
        :return: CustomResponse
        """

        assert self._response.status_code == status_code, f'Got {self._response.status_code} instead of {status_code}'

        return self

    def status_code(self) -> int:
        """
        Get the response status code

        :return: Status code
        """

        return self._response.status_code

    def text(self) -> str:
        """
        Get the response text

        :return: Response text
        """

        return self._response.text

    def response_json(self) -> Any:
        """
        Get the response json

        :return: Response json
        """

        return self._response.json()

    def get_response(self, json_path: str = '$') -> Any:
        """
        Get response

        :param json_path: Json path (e.g. $ is root path)
        :return: Response
        """

        values = self.get_response_list(json_path)
        return values[0] if len(values) == 1 else values

    def get_response_item(self, json_path: str = '$', allow_empty=False) -> Any:
        """
        Get response item

        :param json_path: Json path (e.g. $ is root path)
        :param allow_empty: Specify True if the response can be empty
        :return: Response item
        """

        values = self.get_response_list(json_path, allow_empty)
        if not values:
            return None
        return values[0]

    def get_response_list(self, json_path: str = '$', allow_empty=False) -> List[Any]:
        """
        Get response list

        :param json_path: Json path (e.g. $ is root path)
        :param allow_empty: Specify True if the response can be empty
        :return: Response list
        """

        values = get_json_path(self._response.json(), json_path, allow_empty)
        if not allow_empty:
            assert values, f'Parameter: {json_path} is not found'
        return values

    def validate_json_schema(self, schema: Dict) -> 'CustomResponseV2':
        """
        Validate response json schema

        :param schema: Specified schema as pattern
        :return: CustomResponse
        """

        jsonschema.validate(self._response.json(), schema)

        return self
