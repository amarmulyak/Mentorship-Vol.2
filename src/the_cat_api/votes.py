import requests
from src.utils.utils import cfg


class Votes:
    def __init__(self):
        self.endpoint = f"{cfg().the_cat_api.url}/votes"

    def get_vote(self):
        return requests.get(self.endpoint, headers={"x-api-key": f"{cfg().the_cat_api.x_api_key}"})
