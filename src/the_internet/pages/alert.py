"""
Alert module.
"""

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Alert:
    """
    Class to work with Alert.
    """

    def __init__(self, driver: webdriver) -> None:
        """
        :param driver: webdriver
        """

        self.driver = driver

    def is_present(self, wait_time: int = 10) -> bool:
        """
        Check if alert is present.

        :param wait_time: Specify the time to wait the Alert to show (default is 10)
        :return: True or False
        """

        try:
            self._wait_until_alert_appear(time=wait_time)
            alert_appear = True
        except TimeoutException:
            alert_appear = False
        return alert_appear

    def get_text(self) -> str:
        """
        Get Alert's text.

        :return: Alert's text
        """
        self._wait_until_alert_appear()
        popup = self.driver.switch_to.alert
        return popup.text

    def accept(self) -> None:
        """
        Accept the Alert.

        :return: None
        """

        self._wait_until_alert_appear()
        popup = self.driver.switch_to.alert
        popup.accept()

    def dismiss(self) -> None:
        """
        Dismiss the Alert.

        :return: None
        """

        self._wait_until_alert_appear()
        popup = self.driver.switch_to.alert
        popup.dismiss()
        self._wait_until_alert_disappear()

    def send_keys(self, text: str) -> None:
        """
        Send keys to the Alert's field.

        :param text: Key you want to send
        :return: None
        """

        self._wait_until_alert_appear()
        popup = self.driver.switch_to.alert
        popup.send_keys(text)

    def _wait_until_alert_appear(self, time: int = 10) -> 'Alert':
        """
        Wait until Alert appear.

        :param time: time (default is 10)
        :return: "Alert" object
        """

        return WebDriverWait(self.driver, time).until(
            EC.alert_is_present(), message="Alert is not present"
        )

    def _wait_until_alert_disappear(self, time: int = 10) -> bool:
        """
        Wait until Alert disappear.

        :param time: time (default is 10)
        :return: False in case Alert disappeared
        :raise: Timeout exception is raised in case of Alert is present
        """

        return WebDriverWait(self.driver, time).until_not(
            EC.alert_is_present(), message="Alert is present"
        )
