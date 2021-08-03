import requests
import json

from src.the_cat_api.vote_params_data import VoteValueParam
from requests import Response


class Votes:
    """
    Votes Class
    """
    PATH = "votes"

    def __init__(self, endpoint: str, x_api_key: str):
        self.endpoint = f'{endpoint}/{self.PATH}'
        self.x_api_key = x_api_key

    def get_votes(self, limit: int = None) -> Response:
        params = {}

        if limit:
            params['limit'] = limit

        return requests.get(self.endpoint,
                            headers={"x-api-key": self.x_api_key},
                            params=params)

    def create_vote(self, image_id: str, vote: VoteValueParam) -> Response:
        body = {'image_id': image_id,
                'value': vote.value}

        return requests.post(self.endpoint,
                             headers={'x-api-key': self.x_api_key, 'Content-Type': 'application/json'},
                             data=json.dumps(body))

    def get_specific_vote(self, vote_id: int) -> Response:
        endpoint = f"{self.endpoint}/{vote_id}"

        return requests.get(endpoint,
                            headers={"x-api-key": self.x_api_key})
