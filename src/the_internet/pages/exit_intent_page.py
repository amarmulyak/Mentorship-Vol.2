from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from src.the_internet.pages.entry_ad_page import EntryAd


class ExitIntent(EntryAd):
    _TITLE = EntryAd._PAGE_TITLE
    _POWERED_BY = (By.XPATH, "//a[@target]")

    def get_entry_exit_intent_page(self):
        self.driver.get(f"{self.url}/exit_intent")

    def move_mouse_out_of_viewport(self):
        action = ActionChains(self.driver)
        link = self.find_element(self._POWERED_BY)
        action.move_to_element_with_offset(link, 10, -20).perform()
        # # action.move_by_offset(-5, 0)
        # action.perform()

