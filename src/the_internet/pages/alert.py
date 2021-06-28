"""
Alert module
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Alert:
    """
    Class to work with Alert
    """

    def __init__(self, driver):
        """
        :param driver: webdriver
        """

        self.driver = driver

    def is_present(self, wait_time=10):
        """
        Check if alert is present

        :param wait_time: Specify the time to wait the Alert to show (default is 10)
        :return: True or False
        """

        try:
            self._wait_until_alert_appear(time=wait_time)
            alert_appear = True
        except TimeoutException:
            alert_appear = False
        return alert_appear

    def get_text(self):
        """
        Get Alert's text

        :return: Alert's text
        """
        self._wait_until_alert_appear()
        popup = self.driver.switch_to.alert
        return popup.text

    def accept(self):
        """
        Accept the Alert

        :return: None
        """
        self._wait_until_alert_appear()
        popup = self.driver.switch_to.alert
        popup.accept()

    def dismiss(self):
        """
        Dismiss the Alert

        :return: None
        """
        self._wait_until_alert_appear()
        popup = self.driver.switch_to.alert
        popup.dismiss()
        self._wait_until_alert_disappear()

    def send_keys(self, text):
        """
        Send keys to the Alert's field

        :param text: Key you want to send
        :return: None
        """

        self._wait_until_alert_appear()
        popup = self.driver.switch_to.alert
        popup.send_keys(text)

    def _wait_until_alert_appear(self, time=10):
        """
        Wait until Alert appear

        :param time: time (default is 10)
        :return: "Alert" object
        """
        return WebDriverWait(self.driver, time).until(
            EC.alert_is_present(), message="Alert is not present"
        )

    def _wait_until_alert_disappear(self, time=10):
        """
        Wait until Alert disappear

        :param time: time (default is 10)
        :return: False
        """

        return WebDriverWait(self.driver, time).until_not(
            EC.alert_is_present(), message="Alert is present"
        )
