from locust import HttpUser, task

from src.utils.utils import cfg

class HelloWorldUser(HttpUser):

    @task
    def test_images_search_response_code(self):
        self.client.get(f'{cfg().the_cat_api.url}/images/search',
                        headers={'x-api-key': f'{cfg().the_cat_api.x_api_key}'})
