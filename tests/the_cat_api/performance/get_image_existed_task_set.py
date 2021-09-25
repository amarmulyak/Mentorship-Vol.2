import json

from locust import HttpUser, task, TaskSet, between

from src.utils.utils import cfg

from src.utils.api import CustomResponseV2


class GetImage(TaskSet):
    def __init__(self, parent):
        super().__init__(parent)
        self.token = cfg().the_cat_api.x_api_key

    @task
    def test_images_search(self):
        image_resp = CustomResponseV2(self.client.get('/images/search',
                                                      headers={'x-api-key': self.token}))
        image_id = image_resp.get_response_item('$.[0].id')

        print(image_id)

        body = {'image_id': image_id,
                'value': 1,
                "sub_id": "my-user-1234"}

        vote_resp = CustomResponseV2(self.client.post('/votes',
                                                      headers={'x-api-key': self.token, 'Content-Type': 'application/json'},
                                                      data=json.dumps(body)))

        print(vote_resp.text)


class User(HttpUser):
    wait_time = between(2, 3)
    host = cfg().the_cat_api.url
    tasks = [GetImage]
