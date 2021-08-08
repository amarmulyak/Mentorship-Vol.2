"""
Module to represent Votes endpoint
"""

import logging

import requests
import json

from requests import Response
from http import HTTPStatus

from src.the_cat_api.vote_params_data import VoteValueParam

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

        response = requests.get(self.endpoint,
                                headers={"x-api-key": self.x_api_key},
                                params=params)

        logger.debug(f'Request: GET {self.endpoint} | Params: limit={limit}'
                     f' | Status Code: {response.status_code} | Response: {response.text}')

        assert response.status_code == HTTPStatus.OK

        return response

    def create_vote(self, image_id: str, vote: VoteValueParam) -> Response:
        """
        POST vote request

        :param image_id: Image ID to vote
        :param vote: Vote up (1), vote down (0)
        :return: Response
        """

        body = {'image_id': image_id,
                'value': vote.value}

        response = requests.post(self.endpoint,
                                 headers={'x-api-key': self.x_api_key, 'Content-Type': 'application/json'},
                                 data=json.dumps(body))

        logger.debug(f'Request: POST {self.endpoint} | Body: image_id: {image_id}, value: {vote}'
                     f' | Status Code: {response.status_code} | Response: {response.text}')

        assert response.status_code == HTTPStatus.OK

        return response

    def get_specific_vote(self, vote_id: int) -> Response:
        """
        GET vote request

        :param vote_id: Vote ID
        :return:
        """

        endpoint = f"{self.endpoint}/{vote_id}"

        response = requests.get(endpoint,
                                headers={"x-api-key": self.x_api_key})

        logger.debug(f'Request: GET {self.endpoint}'
                     f' | Status Code: {response.status_code} | Response: {response.text}')

        assert response.status_code == HTTPStatus.OK

        return response
