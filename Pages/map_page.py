import re

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class MapPage(BasePage):
    FITNESS = (By.XPATH, "//button[contains(text(),'Fitness')]")
    FILTER_GYM = (By.XPATH, "//span[text()='Gym']")
    FILTER_POOL = (By.XPATH, "//button[contains(text(),'Pool & beach')]")
    CLEAR_FILTER = (By.XPATH, "//button[text()='Clear filters']")
    VENUE_COUNT = (By.XPATH, "//*[@id='__next']/main/div[1]/h3")
    VENUE_NAME = (By.XPATH, "//h3[contains(text(),'Final Round')]")
    VENUE_DESC = (By.XPATH, "//p[contains(text(),'A full-body workout that’s fast, effective and fun')]")
    FITNESS_BUTTON = (By.XPATH, "//button[contains(text(), 'Fitness')]")
    POOL_BEACH_BUTTON = (By.XPATH, "//button[contains(text(), 'Pool & beach')]")
    FILTER_FITNESS = (By.XPATH, "//h3[contains(text(), 'fitness venues')]")
    FILTER_POOL = (By.XPATH, "//h3[contains(text(), 'pool & beach venues')]")
    FILTER = (By.XPATH, "//button[contains(text(),'Filters')]")
    #SHOW_VENUES_BUTTON = (By.XPATH, "//button[contains(text(),'Show') and contains(text(),'venues')]")
    SHOW_VENUES_BUTTON = (By.XPATH, "//button[@class='sc-5180758e-9 jygJwH']")
    DUBAI_BUTTON = (By.XPATH, "//button[span='Dubai']")

    def apply_filter(self, filter_type):
        """Apply a specific venue filter."""
        if filter_type.lower() == "gym":
            self.click_element(self.FITNESS_BUTTON)
            heading_text = self.get_text(self.FILTER_FITNESS)
        elif filter_type.lower() == "pool":
            self.click_element(self.POOL_BEACH_BUTTON)
            heading_text = self.get_text(self.FILTER_POOL)
        heading_text = re.sub(r'^\d+\s+', '', heading_text)
        return heading_text.strip()  # Return the text without the number

    def get_venue_count(self):
        """Returns the number of visible venues on the map."""
        venue_count_element = self.driver.find_element(*self.VENUE_COUNT)
        venue_text = venue_count_element.text
        match = re.search(r'\d+', venue_text)
        if match:
         # Return the integer value of the number
           return int(match.group())
        return None

    def select_first_venue(self):
        """Click the first venue marker."""
        self.click_element(self.VENUE_NAME)

    def get_venue_details(self):
        """Fetch venue name and description."""
        return {
              "name": self.get_text(self.VENUE_NAME),
              "description": self.get_text(self.VENUE_DESC),
        }

    def reset_filters(self):
        """Click the Reset button to clear filters."""
        self.click_element(self.CLEAR_FILTER)

    def click_filter_button(self):
        self.click_element(self.FILTER)

    def click_show_venue_button(self):
        self.click_element(self.SHOW_VENUES_BUTTON)

    def get_venue_counts(self):
        count1 = self.get_text(self.SHOW_VENUES_BUTTON)
        venue_count = int(re.search(r'\d+', count1).group())
        return venue_count

