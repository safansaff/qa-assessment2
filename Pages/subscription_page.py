from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage

class SubscriptionPage(BasePage):
    #ONE_MONTH_PLAN = (By.XPATH, "//div[contains(@class, 'sc-10306a3a-2')]")
    #TWELVE_MONTH_PLAN = (By.XPATH, "//div[contains(@class, 'sc-10306a3a-2') and contains(@class, 'iEMCTr')]")
    """
    FOUR_MONTH_PLAN = (By.XPATH, "//div[contains(@class, 'sc-10306a3a-2 jwRkHO')]//span[text()='4 "
                                 "months']//following::span[text()='AED 749']/following::span[text()='Beach, Pool, "
                                 "Gym & Padel access']/following::span[text()='Restaurant & Spa "
                                 "discounts']/following::span[text()='Save AED 400']")
    """
    ONE_MONTH_PLAN = (By.XPATH, "//div[contains(text(),'1 month') and contains(text(),'AED 1,099')]")
    TWELVE_MONTH_PLAN = (By.XPATH, "//div[contains(text(),'12 months') and contains(text(),'AED 569/month')]")
    FOUR_MONTH_PLAN = (By.XPATH, "//div[contains(text(),'4 months') and contains(text(),'AED 749/month')]")
    MONTHLY_TWELVE = (By.XPATH, "//*[@id='__next']/article/form/div[2]/div[4]/div[1]/div/div[1]/div/div")
    MONTHLY_FOUR = (By.XPATH, "//*[@id='__next']/article/form/div[2]/div[4]/div[1]/div/div[2]/div/div")
    LATER_MONTHLY_TWELVE = (By.XPATH, "//*[@id='__next']/article/form/div[2]/div[4]/div[1]/div")
    PAY_NOW_ONE = (By.XPATH, "//*[@id='__next']/article/form/div[2]/div[4]/div[1]/div/div[1]/div/div")
    PAY_NOW_TWELVE = (By.XPATH, "//*[@id='__next']/article/form/div[2]/div[4]/div[1]/div/div[2]/div/div")
    PAY_NOW_FOUR = (By.XPATH, "//*[@id='__next']/article/form/div[2]/div[4]/div[1]/div/div[3]/div/div")
    PAY_NOW = (By.XPATH, "//*[@id='__next']/article/form/div[2]/div[3]/div/div[1]")
    PAY_LATER = (By.XPATH, "//*[@id='__next']/article/form/div[2]/div[3]/div/div[2]")
    PAY_MONTHLY = (By.XPATH, "//*[@id='__next']/article/form/div[2]/div[3]/div/div[3]")
    PRICE = (By.XPATH, "/html/body/div[1]/article/form/div[2]/div[4]/div[1]/div/div[1]/div/div/div[1]/div/span/text()")
    DETAILS = (By.XPATH, "//*[@id='__next']/article/form/div[2]/div[4]/div[1]/div/div[1]/div/div/div[3]")

    def click_pay_now(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PAY_NOW)
        )
        self.click_element(self.PAY_NOW)

    def click_elements(self, locator):
        """Helper function to click an element."""
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        # Scroll the element into view to prevent overlap
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # Ensure the element is not blocked by another element (e.g., modal)
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[@class='modal']"))  # Adjust as per your modal locator
        )

        # Use ActionChains to handle click, overcoming potential overlap issues
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def click_pay_later(self):
        self.click_elements(self.PAY_LATER)

    def click_monthly(self):
        self.click_element(self.PAY_MONTHLY)

    def verify_one_month_plan(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ONE_MONTH_PLAN))

    def verify_twelve_month_plan(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.MONTHLY_TWELVE))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.MONTHLY_FOUR))

    def verify_four_month_plan(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FOUR_MONTH_PLAN))

    def get_twelve_month_price_pay_monthly(self):
        price_element = self.find_element(self.PRICE)
        price = price_element.text
        print(f"Price: {price}")

    def get_twelve_month_details_pay_monthly(self):
        details_element = self.find_element(self.DETAILS)
        details = details_element.text
        print(f"Details: {details}")






