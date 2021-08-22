"""
Exit Intent module.
"""

from src.the_internet.pages.modal import Modal
# from src.utils.utils import move_mouse_to


class ExitIntent(Modal):
    """
    Class to represent Exit Intent page.
    """

    def get_exit_intent_page(self) -> None:
        """
        Open Exit Intent page

        :return: None
        """

        self.driver.get(f"{self.url}/exit_intent")

    # @staticmethod
    # def move_mouse_out_of_viewport() -> None:
    #     """
    #     Move mouse cursor from the top of the screen to down and
    #     back to the top of the screen
    #
    #     :return: None
    #     """
    #
    #     move_mouse_to(500, 500)
    #     move_mouse_to(500, 0)
