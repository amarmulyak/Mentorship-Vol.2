from src.the_internet.pages.dynamically_loaded_elements_page_e1 import DynamicallyLoadedElementsPageE1


class DynamicallyLoadedElementsPageE2(DynamicallyLoadedElementsPageE1):
    def get_dynamically_loaded_elements_page2(self):
        return self.driver.get(f"{self.url}/dynamic_loading/2")
