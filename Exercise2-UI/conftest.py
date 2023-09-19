"""
File: conftest.py
Description: Configuration file for pytest and Selenium WebDriver setup.
Author: Roger Pérez Parera
Date: 20th September, 2023
"""

import pytest
from selenium import webdriver

# Pytest command-line option for specifying the browser and full_test option
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser: chrome / firefox / edge")
    parser.addoption("--full_test", action="store", default="False", help="full_test: True / False")
    parser.addoption("--headless", action="store", default="False", help="headless: True / False")
    parser.addoption("--disable-dev-shm-usage", action="store", default="False", help="disable-dev-shm-usage: True / False")

# Fixture to retrieve command-line arguments, the specified browser and the full_test option
@pytest.fixture
def command_line_arguments(request):
    return {
        "browser": request.config.getoption("--browser"),
        "full_test": request.config.getoption("--full_test"),
        "headless": request.config.getoption("--headless"),
        "disable-dev-shm-usage": request.config.getoption("--disable-dev-shm-usage")
        }

# Fixture to initialize and configure the WebDriver based on the chosen browser
@pytest.fixture
def driver(command_line_arguments):
    chrome_options = webdriver.ChromeOptions()
    if command_line_arguments["headless"] == "True": chrome_options.add_argument("--headless")
    if command_line_arguments["disable-dev-shm-usage"] == "True": chrome_options.add_argument("--disable-dev-shm-usage")

    browser_name = command_line_arguments["browser"]
    if browser_name == "chrome":
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "edge":
        driver = webdriver.Edge()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        print("Not a valid browser. Chrome will be used as default without arguments")
        driver = webdriver.Chrome()

    yield driver

    # Quit Webdriver instance
    driver.quit()