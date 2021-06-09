from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    _PAGE_TITLE = (By.XPATH, "//div[@class='example']/h3")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    def wait_until_visible(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Locator {locator} is not visible",
        )

    def wait_until_invisible(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.invisibility_of_element(locator),
            message=f"Locator {locator} is not visible",
        )

    def wait_until_text_in_element(self, locator, text, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.text_to_be_present_in_element(locator, text),
            message=f"Locator {locator} is not visible",
        )

    def wait_until_element_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message=f"Locator {locator} is not clickable",
        )

    def click_on_element(self, locator):
        return self.find_element(locator).click()

    def element_text(self, locator):
        return self.find_element(locator).text

    def element_is_present(self, locator, wait_time=10):
        try:
            self.find_element(locator, time=wait_time)
            element_found = True
        except TimeoutException:
            element_found = False
        return element_found

    def element_is_visible(self, locator, wait_time=10):
        try:
            self.wait_until_visible(locator, time=wait_time)
            element_visible = True
        except TimeoutException:
            element_visible = False
        return element_visible

    def provide_text_to_element(self, locator, text):
        self.find_element(locator).send_keys(text)
