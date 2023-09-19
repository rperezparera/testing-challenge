"""
File: utils.py
Description: Utility functions for Selenium testing.
Author: Roger Pérez Parera
Date: 20th September, 2023
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Utils function to find and return the 'Start Test' button element
def find_start_test_button(driver):
    return driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-green")

# Utils function to find and return the URL input field element
def find_url_field(driver):
    return driver.find_element(By.NAME, "url")

# Utils function to wait for and return the 'metric-overview' element
def wait_until_results(driver, wait_timeout):
    wait = WebDriverWait(driver, wait_timeout)
    results = wait.until(EC.visibility_of_element_located((By.ID, 'metric-overview')))
    return results

# Utils function to wait for and return a notification element
def wait_until_notification(driver, wait_timeout):
    wait = WebDriverWait(driver, wait_timeout)
    notification = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.dbb-notification-notice-content")))
    return notification

# Utils function to wait for and return the waiting room message element
def wait_until_waiting_room(driver, wait_timeout):
    wait = WebDriverWait(driver, wait_timeout)
    waiting_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "css-re4smq")))
    return waiting_message
