from locust import HttpUser, task, TaskSet, between

from src.utils.utils import cfg


class GetImage(TaskSet):

    @task
    def test_images_search_response_code(self):
        self.client.get('/images/search',
                        headers={'x-api-key': f'{cfg().the_cat_api.x_api_key}'})


class User(HttpUser):
    wait_time = between(2, 3)
    host = cfg().the_cat_api.url
    tasks = [GetImage]
