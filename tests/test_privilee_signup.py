import time
import asyncio
import pytest
from Pages.signup_page import SignUpPage
from conftest import setup


async def run_test():
    driver = await setup()
    await test_all_fields(driver)
    await test_mandatory_fields_error_message(driver)
    await test_valid_subscription_form(driver)
    await driver.quit()


@pytest.mark.asyncio
async def test_valid_subscription_form(setup):
    """Test verifies that the subscription form works correctly when valid inputs are provided.
       Expected Outcome : User should navigated to subscription form on entering the required details.
       Importance : This is a basic functionality test to ensure the core feature of submitting
                                   a subscription form with valid input works as expected.
    """
    signup_page = SignUpPage(setup)
    signup_page.join_today_button()
    signup_page.fill_form("John", "john.doe@example.com", "0501234567")

    signup_page.submit_form()
    assert signup_page.get_article(), "Navigation to the expected page failed!"


@pytest.mark.asyncio
async def test_all_fields(setup):
    """Test error messages when all fields are left blank.
       Feature being tested: This test checks if appropriate error messages are shown when all fields are
                             left blank in the form.
       Expected outcome: The form should not submit, and error messages should be displayed for all required
                        fields (name, email, and phone).
       Importance: This is essential to test form validation, ensuring that users cannot submit the form with
                   missing mandatory fields.
    """
    signup_page = SignUpPage(setup)
    signup_page.join_today_button()
    signup_page.fill_form("", "", "")
    signup_page.submit_form()
    #time.sleep(2)

    error_message = signup_page.get_error_message()
    assert len(error_message) > 0, "Required field validation failed!"


@pytest.mark.asyncio
async def test_mandatory_fields_error_message(setup):
    """Test error messages when one of the required field is left blank.
    Feature being tested: This test ensures that error messages are shown when any of the required fields
    (name, email, or phone) are left blank in the subscription form.
    Expected outcome: The form should not submit successfully, and an error message should be displayed for the
                      missing mandatory fields.
    Importance : This test ensures that form validation is functioning correctly for mandatory fields, and it
                 provides a safeguard against incomplete submissions.


    """
    signup_page = SignUpPage(setup)
    test_cases = [
        {"first_name": "John", "email": "", "phone": "589123455", "missing_field": "Email"},
        {"first_name": "John", "email": "abc@p.com", "phone": "", "missing_field": "Phone"}
    ]
    signup_page.join_today_button()
    for test_case in test_cases:
        signup_page.fill_form(first_name=test_case["first_name"], email=test_case["email"], phone=test_case["phone"]
        )
        signup_page.submit_form()

        if test_case["missing_field"] in ["Email", "Phone"]:
            error_message = signup_page.get_error_message()
            print(f"Error message for {test_case['missing_field']}: {error_message}")

        assert len(error_message) > 0, "Required field validation failed!"
        print(f"outside assert")

        signup_page.clear_form()
        print(f"outside clear form")
        signup_page.focus_on_first_name()
    return



