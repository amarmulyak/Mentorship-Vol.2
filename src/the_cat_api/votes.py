import requests
import json

from src.the_cat_api.vote_params_data import VoteValueParam
from requests import Response
from src.utils.utils import cfg


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
                'value': vote.value,
                'sub_id': 'my-user-1234'}

        return requests.post(self.endpoint,
                             headers={'x-api-key': self.x_api_key, 'Content-Type': 'application/json'},
                             data=json.dumps(body))
