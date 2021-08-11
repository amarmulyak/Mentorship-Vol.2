"""
Module to represent Votes endpoint
"""

import json
import logging
from http import HTTPStatus

import requests
from requests import Response

from src.the_cat_api.schema import GET_VOTES_SCHEMA, POST_CREATE_VOTE_SCHEMA
from src.the_cat_api.vote_params_data import VoteValueParam
from src.utils.api import CustomResponse

logger = logging.getLogger()


class Votes:
    """
    Class to represent Votes endpoint
    """

    PATH = "votes"

    def __init__(self, endpoint: str, x_api_key: str):
        self.endpoint = f'{endpoint}/{self.PATH}'
        self.x_api_key = x_api_key

    def get_votes(self, limit: int = None) -> Response:
        """
        GET votes request

        :param limit: Votes limit
        :return: Response
        """

        params = {}

        if limit:
            params['limit'] = limit

        response = CustomResponse(requests.get(self.endpoint,
                                               headers={"x-api-key": self.x_api_key},
                                               params=params))

        logger.debug(f'Request: GET {self.endpoint} | Params: limit={limit}'
                     f' | Status Code: {response.status_code} | Response: {response.text}')

        response.status_code_is(HTTPStatus.OK)

        response.validate_json_schema(GET_VOTES_SCHEMA)

        return response

    def create_vote(self, image_id: str, vote: VoteValueParam) -> Response:
        """
        POST vote request

        :param image_id: Image ID to vote
        :param vote: Vote up (1), vote down (0)
        :return: Response
        """

        body = {'image_id': image_id,
                'value': vote.value,
                "sub_id": "my-user-1234"}

        response = CustomResponse(requests.post(self.endpoint,
                                                headers={'x-api-key': self.x_api_key, 'Content-Type': 'application/json'},
                                                data=json.dumps(body)))

        logger.debug(f'Request: POST {self.endpoint} | Body: image_id: {image_id}, value: {vote}'
                     f' | Status Code: {response.status_code} | Response: {response.text}')

        response.status_code_is(HTTPStatus.OK)

        response.validate_json_schema(POST_CREATE_VOTE_SCHEMA)

        return response

    def get_specific_vote(self, vote_id: int, expected_status_code: int = HTTPStatus.OK) -> Response:
        """
        GET vote request

        :param vote_id: Vote ID
        :param expected_status_code: Expected Status Code
        :return: Response
        """

        endpoint = f"{self.endpoint}/{vote_id}"

        response = requests.get(endpoint,
                                headers={"x-api-key": self.x_api_key})

        logger.debug(f'Request: GET {endpoint}'
                     f' | Status Code: {response.status_code} | Response: {response.text}')

        assert response.status_code == expected_status_code

        return response

    def delete_vote(self, vote_id: str) -> Response:
        """
        DELETE vote request

        :param vote_id: Vote ID
        :return: Response
        """

        endpoint = f"{self.endpoint}/{vote_id}"
        response = requests.delete(endpoint,
                                   headers={"x-api-key": self.x_api_key})

        logger.debug(f'Request: DELETE {endpoint}'
                     f' | Status Code: {response.status_code} | Response: {response.text}')

        assert response.status_code == HTTPStatus.OK

        return response
