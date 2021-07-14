"""
Home page module.
"""

from selenium.webdriver.common.by import By

from src.the_internet.pages.ab_testing_page import ABTestingPage
from src.the_internet.pages.add_remove_elements_page import AddRemoveElementsPage
from src.the_internet.pages.base_page import BasePage
from src.the_internet.pages.basic_auth_page import BasicAuthPage
from src.the_internet.pages.broken_images_page import BrokenImagesPage
from src.the_internet.pages.challenging_dom_page import ChallengingDomPage
from src.the_internet.pages.context_menu_page import ContextMenuPage
from src.the_internet.pages.digest_auth_page import DigestAuthPage
from src.the_internet.pages.drag_and_drop_page import DragAndDropPage
from src.the_internet.pages.dynamic_controls_page import DynamicControlsPage
from src.the_internet.pages.dynamically_loaded_elements_page import (
    DynamicallyLoadedElementsPage,
)


class HomePage(BasePage):
    """
    Class to represent Home page.
    """

    home_page_title_locator = (By.CLASS_NAME, "heading")
    example_link_locator = (By.XPATH, "//a[contains(text(), '{}')]")

    def get_home_page(self) -> None:
        """
        Open Home page.

        :return: None
        """

        return self.driver.get(f"{self.url}")

    def get_home_page_title_text(self) -> str:
        """
        Get the page title text.

        :return: Page title text
        """

        return self.get_element_text(self.home_page_title_locator)

    def click_ab_testing_link(self) -> ABTestingPage:
        """
        Click the "A/B Testing" link.

        :return: ABTestingPage
        """

        self.click_on_element(
            (
                self.example_link_locator[0],
                self.example_link_locator[1].format("A/B Testing"),
            )
        )
        return ABTestingPage(self.driver)

    def click_add_remove_elements_link(self) -> AddRemoveElementsPage:
        """
        Click the "Add/Remove Elements" link.

        :return: AddRemoveElementsPage
        """

        self.click_on_element(
            (
                self.example_link_locator[0],
                self.example_link_locator[1].format("Add/Remove Elements"),
            )
        )
        return AddRemoveElementsPage(self.driver)

    def click_basic_auth_link(self) -> BasicAuthPage:
        """
        Click the "Basic Auth" link.

        :return: BasicAuthPage
        """

        self.click_on_element(
            (
                self.example_link_locator[0],
                self.example_link_locator[1].format("Basic Auth"),
            )
        )
        return BasicAuthPage(self.driver)

    def click_broken_images_link(self) -> BrokenImagesPage:
        """
        Click the "Broken Images" link.

        :return: BrokenImagesPage
        """

        self.click_on_element(
            (
                self.example_link_locator[0],
                self.example_link_locator[1].format("Broken Images"),
            )
        )
        return BrokenImagesPage(self.driver)

    def click_challenging_dom_link(self) -> ChallengingDomPage:
        """
        Click the "Challenging DOM" link.

        :return: ChallengingDomPage
        """

        self.click_on_element(
            (
                self.example_link_locator[0],
                self.example_link_locator[1].format("Challenging DOM"),
            )
        )
        return ChallengingDomPage(self.driver)

    def click_context_menu_link(self) -> ContextMenuPage:
        """
        Click the "Context Menu" link.

        :return: ContextMenuPage
        """

        self.click_on_element(
            (
                self.example_link_locator[0],
                self.example_link_locator[1].format("Context Menu"),
            )
        )
        return ContextMenuPage(self.driver)

    def click_digest_auth_link(self) -> DigestAuthPage:
        """
        Click the "Digest Authentication" link.

        :return: DigestAuthPage
        """

        self.click_on_element(
            (
                self.example_link_locator[0],
                self.example_link_locator[1].format("Digest Authentication"),
            )
        )
        return DigestAuthPage(self.driver)

    def click_drag_and_drop_link(self) -> DragAndDropPage:
        """
        Click the "Drag and Drop" link.

        :return: DragAndDropPage
        """

        self.click_on_element(
            (
                self.example_link_locator[0],
                self.example_link_locator[1].format("Drag and Drop"),
            )
        )
        return DragAndDropPage(self.driver)

    def click_dynamic_controls_link(self) -> DynamicControlsPage:
        """
        Click the "Dynamic Controls" link.

        :return: DynamicControlsPage
        """

        self.click_on_element(
            (
                self.example_link_locator[0],
                self.example_link_locator[1].format("Dynamic Controls"),
            )
        )
        return DynamicControlsPage(self.driver)

    def click_dynamic_loading_link(self) -> DynamicallyLoadedElementsPage:
        """
        Click the "Dynamic Loading" link.

        :return: DynamicallyLoadedElementsPage
        """

        self.click_on_element(
            (
                self.example_link_locator[0],
                self.example_link_locator[1].format("Dynamic Loading"),
            )
        )
        return DynamicallyLoadedElementsPage(self.driver)
