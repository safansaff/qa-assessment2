import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def setup():
    """Set up WebDriver before each test and close it after."""
    #driver = webdriver.Chrome(executable_path="C:\\Users\\anany\\Downloads\\chromedriver_win32")
    service = Service(executable_path="C:\\Users\\anany\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    #driver.maximize_window()
    driver.get("https://staging-website.privilee.ae/map")
    yield driver
    driver.quit
