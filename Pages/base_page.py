from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        field = self.find_element(locator)
        field.clear()
        field.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text