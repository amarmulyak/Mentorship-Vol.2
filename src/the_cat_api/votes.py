import requests


class Votes:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def get_vote(self):
        return requests.get(self.endpoint, headers={"x-api-key": "0a3b91c0-81d1-46f9-9671-ce0d71b354f8"})
