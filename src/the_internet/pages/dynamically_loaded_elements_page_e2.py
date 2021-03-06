"""
Dynamically loaded elements - Example 2 module.
"""

from src.the_internet.pages.dynamically_loaded_elements_page_e1 import DynamicallyLoadedElementsPageE1


class DynamicallyLoadedElementsPageE2(DynamicallyLoadedElementsPageE1):
    """
    Class to represent Dynamically loaded elements - Example 2 page.
    """

    def get_dynamically_loaded_elements_page2(self) -> None:
        """
        Open page.

        :return: None
        """

        return self.driver.get(f"{self.url}/dynamic_loading/2")
