from src.the_internet.pages.dynamically_loaded_elements_page1 import DynamicallyLoadedElementsPage1


class DynamicallyLoadedElementsPage2(DynamicallyLoadedElementsPage1):
    def get_dynamically_loaded_elements_page2(self):
        return self.driver.get(f"{self.path}/dynamic_loading/2")
