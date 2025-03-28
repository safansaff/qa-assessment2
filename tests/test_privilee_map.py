import re
import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Pages.map_page import MapPage
from conftest import setup
from selenium.webdriver.support import expected_conditions as EC
from Pages.signup_page import SignUpPage


async def run_test():
    driver = await setup()
    await test_filter_and_reset(driver)
    await test_venue_details(driver)
    await test_map_performance(driver)
    await driver.quit()


@pytest.mark.asyncio
async def test_filter_and_reset(setup):
    """Test if filtering works correctly.
    Feature being tested: This test checks the functionality of the filter and reset options on the map
    page, ensuring that the correct venues are displayed and that the reset functionality works as expected.

   Expected outcome:When a filter is applied, the displayed venues should match the filter category
   (e.g., "fitness venues" or "pool & beach venues").After applying the filter, the venue count should
   decrease when a specific location (e.g., Dubai) is selected. When the filter is reset, the venue count
   should return to its original value.

  Importance: Filtering is a key feature for improving the user experience, as it allows users to quickly
  narrow down their options based on preferences. Ensuring the filters work correctly and reset properly
  is crucial for user satisfaction and data integrity.
    """
    map_page = MapPage(setup)
    applied_text = map_page.apply_filter("gym")
    assert applied_text == "fitness venues", f"Expected 'fitness venues', but got {applied_text}"

    # Apply 'pool' filter and check if the heading text is correct
    applied_text = map_page.apply_filter("pool")  # Apply the pool filter
    assert applied_text == "pool & beach venues", f"Expected 'pool & beach venues', but got {applied_text}"

    map_page.click_filter_button()
    driver = setup
    driver.execute_script("document.body.style.zoom='80%'")

    before_filter = map_page.get_venue_counts()
    map_page.click_element(map_page.DUBAI_BUTTON)
    after_filter = map_page.get_venue_counts()
    assert int(after_filter) < int(before_filter), f"Filter was not applied properly: {after_filter} is not less than {before_filter}"

    # Reset filters
    map_page.reset_filters()
    restored_count = map_page.get_venue_counts()
    assert int(restored_count) == int(before_filter), f"Filter was not reset properly: {restored_count} is not same as {before_filter}"


@pytest.mark.asyncio
async def test_venue_details(setup):
    """Test if venue details are displayed correctly.
    Feature being tested: This test checks if the venue details (name and description) are displayed
    correctly when a venue is selected from the map.

    Expected outcome: When a venue is selected, its name and description should be displayed and not be empty.
                      The form should be filled out with valid user information before viewing the venue details.
    Importance: Displaying accurate and detailed venue information is vital for providing a seamless user
    experience. Users depend on this information to make decisions, so verifying that it is displayed correctly ensures the platform’s reliability and quality.
    """
    map_page = MapPage(setup)
    signup_page = SignUpPage(setup)
    map_page.apply_filter("gym")
    map_page.select_first_venue()
    signup_page.fill_form("Test", "abc@p.com", "5555555667")
    signup_page.view_button()
    details = map_page.get_venue_details()
    assert details["name"] != "", "Venue name is missing"
    assert details["description"] != "", "Venue description is missing"


@pytest.mark.asyncio
async def test_map_performance(setup):
    """Test if the map loads quickly with multiple venues.
    Feature being tested: This test checks the performance of the map, specifically focusing on how quickly
    it loads and how many venues are displayed.
    Expected outcome: The map should load with more than 10 venues.
                      The load time of the map should be under 5 seconds.
    Importance: Performance is a crucial aspect of any web or mobile application. A slow-loading map can
                frustrate users. This test ensures that the map performs well and that the user experience
                is optimized by reducing load times.
    """
    map_page = MapPage(setup)
    start_time = time.time()

    venues = int(map_page.get_venue_count())
    assert venues > 10, "Not enough venues loaded"
    print(f"venue count : {venues}")

    load_time = time.time() - start_time
    assert load_time < 5, f"Map took too long to load: {load_time} seconds"
    print(f"load_time : {load_time}")