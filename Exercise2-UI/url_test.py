"""
File: url_test.py
Description: Test script for testing positive and negative cases with different URL variations.
Author: Roger Pérez Parera
Date: 20th September, 2023
"""

import pytest
from utils import find_start_test_button, find_url_field, wait_until_results, wait_until_notification

# Base URL
base_url = "https://www.debugbear.com/test/website-speed"
# Wait timeout in seconds
wait_timeout = 100

# ===========================
# ======== POSITIVE  ========
# ======== SCENARIO  ========
# ===========================
@pytest.mark.parametrize("url", [
    # Test Case 1: Send the intact test URL. 
    ("https://es.idoven.ai/"),

    # Test Case 2: Send the test URL without the protocol. 
    ("es.idoven.ai/"),

    # Test Case 3: Send the test URL without the protocol and without slashes. 
    ("es.idoven.ai"),

    # Test Case 4: Send the test URL with a combination of uppercase and lowercase letters. 
    ("https://Es.IdOvEn.Ai/"), 

    # Test Case 5: Send the test URL with a leading whitespace. 
    (" https://es.idoven.ai/"),

    # Test Case 6: Send the test URL with a trailing whitespace. 
    ("https://es.idoven.ai/ ")
])
# Expected Results: Successful speed test functionality completed
def test_speed_test_url_positive_scenario(driver, command_line_arguments, url):
    # Skip if full test mode was not selected
    if command_line_arguments["full_test"] != "True": pytest.skip("Skip test since we are on reduced coverage mode")

    # Open the Webdriver
    driver.get(base_url)

    # Locate the URL field and the start button
    url_input = find_url_field(driver)
    start_test_button = find_start_test_button(driver)

    # Enter the URL and click the start button
    url_input.send_keys(url)
    start_test_button.click()

    # Wait for the test to complete
    results = wait_until_results(driver, wait_timeout)

    # If results are not received, fail
    assert results 

# ===========================
# ======== NEGATIVE  ========
# ======== SCENARIO  ========
# ===========================
@pytest.mark.parametrize("url, expected_message", [
    # Test Case 1: Send the test url incomplete
    ("esidovenai", "URL must include '.'."),

    # Test Case 2: Send a url with the 'idoven' word but invalid
    ("www.idoven.abc", "Failed to resolve URL"),

    # Test Case 3: Send the test url with a wrong protocol
    ("htt://es.idoven.ai/", "Failed to resolve URL"),

    # Test Case 4: Send an empty url
    ("", "Enter a website URL to start the performance test")
])
# Expected Results: Test functionality not completed and a notification message received
def test_speed_test_url_negative_scenario(driver, url, expected_message):
    # Open the Webdriver
    driver.get(base_url)

    # Locate the URL field and the start button
    url_input = find_url_field(driver)
    start_test_button = find_start_test_button(driver)

    # Enter the URL and click the start button
    url_input.send_keys(url)
    start_test_button.click()

    # Wait for the notification to be received
    notification = wait_until_notification(driver, 10)

    # If notification is not received matching the expected text, fail
    assert expected_message in notification.text    