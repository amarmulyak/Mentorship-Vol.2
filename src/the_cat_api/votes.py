import requests
from src.utils.utils import cfg


class Votes:
    """
    Votes Class
    """
    PATH = "votes"

    def __init__(self, endpoint: str, x_api_key: str):
        self.endpoint = f'{endpoint}/{self.PATH}'
        self.x_api_key = x_api_key

    def get_votes(self, limit: int = None):
        params = {}

        if limit:
            params['limit'] = limit

        return requests.get(self.endpoint,
                            headers={"x-api-key": self.x_api_key},
                            params=params)
