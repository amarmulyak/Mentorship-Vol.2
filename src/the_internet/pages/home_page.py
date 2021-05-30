from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage
from src.the_internet.pages.ab_testing_page import ABTestingPage
from src.the_internet.pages.add_remove_elements_page import AddRemoveElementsPage
from src.the_internet.pages.basic_auth_page import BasicAuthPage
from src.the_internet.pages.broken_images_page import BrokenImagesPage
from src.the_internet.pages.challenging_dom_page import ChallengingDomPage
from src.the_internet.pages.context_menu_page import ContextMenuPage
from src.the_internet.pages.digest_auth_page import DigestAuthPage
from src.the_internet.pages.drag_and_drop_page import DragAndDropPage
from src.the_internet.pages.dynamic_controls_page import DynamicControlsPage


class HomePage(BasePage):
    home_page_title_locator = (By.CLASS_NAME, "heading")
    ab_testing_link_locator = (By.XPATH, "//a[contains(text(), 'A/B Testing')]")
    example_link_locator = (By.XPATH, "//a[contains(text(), '{}')]")

    def get_home_page(self):
        return self.driver.get("https://the-internet.herokuapp.com/")

    def home_page_title_equal(self, text):
        return self.element_text_equal(self.home_page_title_locator, text)

    def click_ab_testing_link(self):
        self.click_on_element((
            self.example_link_locator[0],
            self.example_link_locator[1].format("A/B Testing")
        ))
        return ABTestingPage(self.driver)

    def click_add_remove_elements_link(self):
        self.click_on_element((
            self.example_link_locator[0],
            self.example_link_locator[1].format("Add/Remove Elements")
        ))
        return AddRemoveElementsPage(self.driver)

    def click_basic_auth_link(self):
        self.click_on_element((
            self.example_link_locator[0],
            self.example_link_locator[1].format("Basic Auth")
        ))
        return BasicAuthPage(self.driver)

    def click_broken_images_link(self):
        self.click_on_element((
            self.example_link_locator[0],
            self.example_link_locator[1].format("Broken Images")
        ))
        return BrokenImagesPage(self.driver)

    def click_challenging_dom_link(self):
        self.click_on_element((
            self.example_link_locator[0],
            self.example_link_locator[1].format("Challenging DOM")
        ))
        return ChallengingDomPage(self.driver)

    def click_context_menu_link(self):
        self.click_on_element((
            self.example_link_locator[0],
            self.example_link_locator[1].format("Context Menu")
        ))
        return ContextMenuPage(self.driver)

    def click_digest_auth_link(self):
        self.click_on_element((
            self.example_link_locator[0],
            self.example_link_locator[1].format("Digest Authentication")
        ))
        return DigestAuthPage(self.driver)

    def click_drag_and_drop_link(self):
        self.click_on_element((
            self.example_link_locator[0],
            self.example_link_locator[1].format("Drag and Drop")
        ))
        return DragAndDropPage(self.driver)

    def click_dynamic_controls_link(self):
        self.click_on_element((
            self.example_link_locator[0],
            self.example_link_locator[1].format("Dynamic Controls")
        ))
        return DynamicControlsPage(self.driver)
