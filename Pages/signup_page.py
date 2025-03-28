from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.base_page import BasePage


class SignUpPage(BasePage):
    # Locators for Signup Form
    FIRST_NAME_FIELD = (By.NAME, "first_name")
    EMAIL_FIELD = (By.NAME, "email")
    PHONE_FIELD = (By.NAME, "mobile")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(),'Thank you')]")  # Adjust based on actual success message
    ERROR_MESSAGE = (By.XPATH, "//div[contains(text(), 'An error occurred')]")
    JOIN_Button = (By.PARTIAL_LINK_TEXT, "Join Privilee")
    ARTICLE = (By.XPATH, "//*[@id='__next']/article")
    VIEW_BUTTON = (By.XPATH, "//button[text()='View']")

    def fill_form(self, first_name, email, phone):
        """Fills the Join form."""
        #self.click_element(self.JOIN_Button)
        self.enter_text(self.FIRST_NAME_FIELD, first_name)
        self.enter_text(self.EMAIL_FIELD, email)
        self.enter_text(self.PHONE_FIELD, phone)

    def join_today_button(self):
        return self.click_element(self.JOIN_Button)

    def submit_form(self):
        """Clicks the submit button."""
        self.click_element(self.SUBMIT_BUTTON)

    def view_button(self):
        self.click_element(self.VIEW_BUTTON)

    def get_success_message(self):
        """Fetches the success message after form submission."""
        return self.get_text(self.SUCCESS_MESSAGE)

    def get_error_message(self):
        """Fetches the error message after form submission"""
        return self.get_text(self.ERROR_MESSAGE)

    def get_article(self):
        """Returns the article element and checks if it is displayed."""
        try:
            article_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.ARTICLE)
            )
            #article_element = self.driver.find_element(self.ARTICLE)
            return article_element.is_displayed()
        except NoSuchElementException:
            return False

    def clear_form(self):
        self.find_element(self.FIRST_NAME_FIELD).clear()
        self.find_element(self.EMAIL_FIELD).clear()
        self.find_element(self.PHONE_FIELD).clear()

    def focus_on_first_name(self):
        first_name_field = self.driver.find_element(*self.FIRST_NAME_FIELD)
        first_name_field.click()

