"""
File: debugBear_test.py
Description: Test cases for the DebugBear speed testing website
Author: Roger Pérez Parera
Date: 20th September, 2023
"""
from utils import find_start_test_button, find_url_field, wait_until_results, wait_until_waiting_room
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import pytest

# Base URL
base_url = "https://www.debugbear.com/test/website-speed"
# Test url
test_url = "https://es.idoven.ai/"
# Wait timeout in seconds
wait_timeout = 600
# Page loading timeout in miliseconds
page_timeout = 10000

# Test Case 1: Load the page and check the page load time
# Expected Result: Loading time less than {page_timeout}
def test_page_loading(driver):
    # Open the Webdriver
    driver.get(base_url)

    page_load_time = driver.execute_script("return performance.timing.loadEventEnd - performance.timing.navigationStart")
    assert page_load_time < page_timeout
    
# Test Case 2: Load the page and check the page title
# Expected Result: Website title to be "Free Website Speed Test | DebugBear"
def test_check_website_title(driver):
    # Open the Webdriver
    driver.get(base_url)

    assert driver.title == "Free Website Speed Test | DebugBear"

# Test Case 3: Check that the url field works. Check if the Start Test button exists and if it has the right text
# Expected Result: URL present in URL field
def test_check_input_text(driver):
    # Open the Webdriver
    driver.get(base_url)

    # Locate the URL field and enter the URL
    url_input = find_url_field(driver)
    url_input.send_keys(test_url)

    assert url_input.get_attribute("value") == test_url

# Test Case 4: Check if the Start Test button exists and if it has the right text
# Expected Result: Start button exists with "Start Test" text
def test_check_start_button(driver):
    # Open the Webdriver
    driver.get(base_url)

    # Locate the start button
    start_test_button = find_start_test_button(driver)
    
    assert start_test_button

    assert start_test_button.text == "Start Test"

# Test Case 5: Load the page and write the test url. Click the Start Test button. Check if we get into the waiting room (loading window)
# Expected Result: To get to the waiting room (loading window)
def test_waiting_room(driver):
    # Open the Webdriver
    driver.get(base_url)

    # Locate the URL field and the start button
    url_input = find_url_field(driver)
    start_test_button = find_start_test_button(driver)

    # Enter the URL and click the start button
    url_input.send_keys(test_url)
    start_test_button.click()

    # Wait for the waiting room
    waiting_message = wait_until_waiting_room(driver, 20)

    assert waiting_message

# Test Case 6: Load the page and write the test url. Click the Start Test button. Check if we get the results
# Expected Result: To get the speed results
def test_response(driver):
    # Open the Webdriver
    driver.get(base_url)

    # Locate the URL field and the start button
    url_input = find_url_field(driver)
    start_test_button = find_start_test_button(driver)

    # Enter the URL and click the start button
    url_input.send_keys(test_url)
    start_test_button.click()

    # Wait for the results
    wait_until_results(driver, wait_timeout)
    
    # Check the result speed report is present
    assert driver.find_element(By.CSS_SELECTOR, "h2.mb-1.mr-1")
    assert driver.title == "es.idoven.ai | DebugBear"

# Test Case 7: Load the page and write the test url. Double click the Start Test button. Check if we get the results
# Expected Result: To get the speed results
def test_speed_test_double_click(driver, command_line_arguments):
    # Skip if full test mode was not selected
    if command_line_arguments["full_test"] != "True": pytest.skip("Skip test since we are on reduced coverage mode")

    # Open the Webdriver
    driver.get(base_url)

    # Locate the URL field and the start button
    url_input = find_url_field(driver)
    start_test_button = find_start_test_button(driver)

    # Enter the URL
    url_input.send_keys(test_url)

    # Double click the start button
    action = ActionChains(driver)
    action.double_click(start_test_button).perform()

    # Wait for the results
    results = wait_until_results(driver, wait_timeout)

    assert results

# Test Case 8: Load the page and write the test url. Hold and click the Start Test button. Check if we get the results
# Expected Result: To get the speed results
def test_speed_test_click_and_hold(driver, command_line_arguments):
    # Skip if full test mode was not selected
    if command_line_arguments["full_test"] != "True": pytest.skip("Skip test since we are on reduced coverage mode")

    # Open the Webdriver
    driver.get(base_url)

    # Locate the URL field and the start button
    url_input = find_url_field(driver)
    start_test_button = find_start_test_button(driver)

    # Enter the URL
    url_input.send_keys(test_url)

    # Hold and click the start button
    action = ActionChains(driver)
    action.click_and_hold(start_test_button).perform()

    # Wait for the results
    results = wait_until_results(driver, wait_timeout)

    assert results     