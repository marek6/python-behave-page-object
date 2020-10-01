from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from features.config import NORMAL


class BasePage(object):
    wait_time = NORMAL

    def __init__(self, driver):
        self.driver = driver

    def send_keys(self, element, value):
        self.driver.find_element(*element).send_keys(value)

    def click_element(self, element):
        self.driver.find_element(*element).click()

    def wait_for_element_to_be_clickable(self, element, time=wait_time):
        WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(element)
        )

    def is_element_visible(self, element, time=wait_time):
        try:
            WebDriverWait(self.driver, time).until(
                EC.visibility_of_element_located(element)
            )
            return True
        except TimeoutException:
            return False
