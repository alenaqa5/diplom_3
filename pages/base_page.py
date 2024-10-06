from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.time = 10

    MODEL_OVERLAY = [By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"]

    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, self.time).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_element_to_be_clickable(self, locator) -> WebElement:
        WebDriverWait(self.driver, self.time).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def wait_element_disappeared(self, overlay=MODEL_OVERLAY):
        self.driver.execute_script("arguments[0].style.display = 'none';", self.driver.find_element(*overlay))
        WebDriverWait(self.driver, self.time).until_not(expected_conditions.visibility_of_element_located(overlay))

    def wait_url_to_be_loaded(self, url):
        WebDriverWait(self.driver, self.time).until(expected_conditions.url_to_be(url))

    def is_element_visible(self, locator):
        try:
            element = WebDriverWait(self.driver, self.time).until(
                expected_conditions.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def is_element_not_visible(self, locator):
        return not self.is_element_visible(locator)

