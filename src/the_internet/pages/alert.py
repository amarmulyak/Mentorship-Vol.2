from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Alert:
    def __init__(self, driver):
        self.driver = driver

    def is_present(self, wait_time=10):
        try:
            self._wait_until_alert_appear(time=wait_time)
            alert_appear = True
        except TimeoutException:
            alert_appear = False
        return alert_appear

    def get_text(self):
        self._wait_until_alert_appear()
        popup = self.driver.switch_to.alert
        return popup.text

    def accept(self):
        self._wait_until_alert_appear()
        popup = self.driver.switch_to.alert
        popup.accept()

    def dismiss(self):
        self._wait_until_alert_appear()
        popup = self.driver.switch_to.alert
        popup.dismiss()

    def send_keys(self, text):
        self._wait_until_alert_appear()
        popup = self.driver.switch_to.alert
        popup.send_keys(text)

    def _wait_until_alert_appear(self, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.alert_is_present(), message="Alert is not present"
        )

    def _wait_until_alert_disappear(self, time=10):
        return WebDriverWait(self.driver, time).until_not(EC.alert_is_present())
