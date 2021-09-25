from locust import HttpUser, task

from src.the_cat_api.images import Images
from src.utils.utils import cfg

class HelloWorldUser(HttpUser):

    @task
    def test_images_search_response_code(self):
        images = Images(cfg().the_cat_api.url, cfg().the_cat_api.x_api_key, http_client=self.client)
        resp = images.get_images()
        print(resp.text)
