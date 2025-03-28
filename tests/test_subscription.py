import time

import pytest
from Pages.subscription_page import SubscriptionPage
from conftest import setup
from Pages.signup_page import SignUpPage


async def run_test():
    driver = await setup()
    await test_subscription(driver)
    await driver.quit()


@pytest.mark.asyncio
async def test_subscription(setup):
    """
    Feature being tested: This test checks the functionality of the subscription process, testing different
    subscription options like "Pay Now," "Pay Later," and "Pay Monthly." It verifies that the correct
    subscription plans are displayed based on the selected option.
   Expected outcome: The form should be successfully submitted with valid details (first name, email, and
   phone number).After submission, the navigation should redirect the user to the appropriate subscription page.
   Based on the selected subscription option (Pay Now, Pay Later, Pay Monthly), the corresponding
   subscription plans should be displayed correctly.
   Importance: This test is critical for verifying that users can subscribe to the correct plans and that
   the system displays the proper subscription options based on their choice. It ensures the functionality
   of different subscription models and checks if the correct plans are available, providing the user
   with accurate choices and a smooth subscription experience.
    """
    signup_page = SignUpPage(setup)
    signup_page.join_today_button()
    signup_page.fill_form("Test", "abcyd@p.com", 564264564)
    signup_page.submit_form()
    time.sleep(7)
    assert signup_page.get_article(), "Navigation to the expected page failed!"

    selected_subscription = "Pay Monthly"  # Change this value to "Pay Now", "Pay Later", or "Pay Monthly"

    if selected_subscription == "Pay Now":
        await handle_pay_now(setup)
    elif selected_subscription == "Pay Later":
        await handle_pay_later(setup)
    elif selected_subscription == "Pay Monthly":
        await handle_pay_monthly(setup)
    else:
        print("Invalid option selected")


@pytest.mark.asyncio
async def handle_pay_now(driver):
    subscription_page = SubscriptionPage(driver)

    element = driver.find_element(*subscription_page.PAY_NOW_ONE)
    assert element.is_displayed(), "1-month plan is not visible"

    element1 = driver.find_element(*subscription_page.PAY_NOW_TWELVE)
    assert element1.is_displayed(), "12-month plan is not visible"

    element2 = driver.find_element(*subscription_page.PAY_NOW_FOUR)
    assert element2.is_displayed(), "4-month plan is not visible"


@pytest.mark.asyncio
async def handle_pay_later(driver):
    subscription_page = SubscriptionPage(driver)
    subscription_page.click_pay_later()
    element = driver.find_element(*subscription_page.LATER_MONTHLY_TWELVE)
    assert element.is_displayed(), "12-months plan is not visible"
    print("Test 'Pay Later' Passed: Only 12-month plan is visible.")


@pytest.mark.asyncio
async def handle_pay_monthly(driver):
    subscription_page = SubscriptionPage(driver)
    subscription_page.click_monthly()
    element = driver.find_element(*subscription_page.MONTHLY_TWELVE)
    assert element.is_displayed(), "12-months plan is not visible"
    element1 = driver.find_element(*subscription_page.MONTHLY_FOUR)
    assert element1.is_displayed(), "4-months plan is not visible"
    print("Test 'Pay Monthly' Passed: 12 and 4-month plans are visible.")
