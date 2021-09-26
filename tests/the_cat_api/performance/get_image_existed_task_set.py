from locust import HttpUser, task, TaskSet, between

from src.the_cat_api.images import Images
from src.the_cat_api.vote_params_data import VoteValueParam
from src.the_cat_api.votes import Votes
from src.utils.utils import cfg


class GetImage(TaskSet):

    @task
    def test_images_search(self):
        images = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key, http_client=self.client)
        votes = Votes(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key, http_client=self.client)
        image_id = images.get_images().get_response_item('$.[0].id')
        resp = votes.create_vote(image_id, VoteValueParam.VALUE_UP)
        print(resp.text)


class User(HttpUser):
    wait_time = between(2, 3)
    host = cfg().the_cat_api.url
    tasks = [GetImage]
