import requests
from src.utils.utils import cfg


class Images:
    def __init__(self):
        self.endpoint = f"{cfg().the_cat_api.url}/images/search"

    def get_images_search(self, size):
        params = {}
        if size:
            # params = {"size": f"{size}"}
            params["size"] = size
        return requests.get(self.endpoint, headers={"x-api-key": f"{cfg().the_cat_api.x_api_key}"}, params=params)
