# TESTING STRATEGY

## Overview

The objective of this testing strategy is to evaluate the speed test tool 'https://www.debugbear.com/test/website-speed' for the website 'https://es.idoven.ai/'. The tool is designed to test the speed of any provided website. This strategy aims to ensure that the speed test functionality (including URL input and the 'start test' button) works effectively, measures website speed, handles various scenarios and provides  results.

## Testing structure

│   conftest.py
│   debugBear_test.py
│   url_test.py
│   utils.py

All scripts covering this testing strategy are present in the same directory. debugBear_test.py and url_test.py add test the test coverage for different scenarios; conftest.py is the standard pytest config file that is required to assist the scenarios; utils.py hold the utility methods to execute the coverage. In more detail:
- **debugBear_test.py**. Test cases for the DebugBear speed testing website. Include the following test cases:
	- Test Case 1: Load the page and check the page load time
	- Test Case 2: Load the page and check the page title
	- Test Case 3: Check that the url field works. Check if the Start Test button exists and if it has the right text
	- Test Case 4: Check if the Start Test button exists and if it has the right text
	- Test Case 5: Load the page and write the test url. Click the Start Test button. Check if we get into the waiting room (loading window)
	- Test Case 6: Load the page and write the test url. Click the Start Test button. Check if we get the results
	- Test Case 7: Load the page and write the test url. Double click the Start Test button. Check if we get the results
	- Test Case 8: Load the page and write the test url. Hold and click the Start Test button. Check if we get the results
- **url_test.py**. Test script for testing positive and negative cases with different URL variations. 
	- Tests 6 different valid variations of the test url 'https://es.idoven.ai/'. Expect pass.
	- Test 4 different invalid variations of the test url. Expect fail.
- **conftest.py**. Configuration file for pytest and Selenium WebDriver setup.
- **utils.py**. Utility functions for Selenium testing.
	
## Testing limitations
'https://www.debugbear.com/test/website-speed' might limitate your ability to perform operations with Selenium due to the number of requests. This means the test scripts could fail because the responses and behaviour would be different.
That's why the number of positive and negative cases in url_test.py have been reduced. 
Also there is implemented a command line argument to switch between full test mode or reduced test mode. The default value is reduced mode. 

Another limitation is the capability of the user's computer to launch a specific browser test. This is why the implementation cover Chrome, Edge and Firefox. A command line argument also allows the user to choose between them, being Chrome the default option.

For more about this, please see HOW TO RUN TESTS section.

# Conclusion
This testing strategy is meant to evaluate the speed test tool available at 'https://www.debugbear.com/test/website-speed' when used to assess the website 'https://es.idoven.ai/'. 

The testing structure is organized into specific test scripts, each catering to different aspects of the speed testing process. The 'debugBear_test.py' script contains the test cases designed to evaluate the behavior of the DebugBear under various conditions. It covers interactions with the website, checks for specific elements, and validates expected behaviors.

Additionally, the 'url_test.py' script focuses on testing different URL variations, both valid and invalid, to test the tool's URL handling capabilities. This script ensures that it can handle different URL inputs.

To address potential limitations, the strategy incorporates flexibility. It offers a reduced test mode to mitigate the risk of triggering restrictions due to a high number of requests to the website. Users can also choose their preferred browser (Chrome, Edge, or Firefox) to accommodate system-specific constraints.

# HOW TO RUN TESTS

## Requirements

- python
- pytest
- selenium

## Run Tests

Go to Exercise2-UI

```bash
pytest
```

This should execute all test cases in Exercise2-UI. It is important to be in Exercise2-UI to execute the pytest command.

## Command line arguments
If 
```bash
pytest -h
```

We can get command-line help. In conftest.py there is implemented 4 custom arguments:
Custom options:
  --browser=BROWSER     browser: chrome / firefox / edge
  --full_test=FULL_TEST
                        full_test: True / False
  --headless=HEADLESS   headless: True / False
  --disable-dev-shm-usage=DISABLE_DEV_SHM_USAGE
						disable-dev-shm-usage = True / False
						
- browser. The user can choose between chrome, firefox or edge. Chrome is the default option. Example for firefox:
```bash
pytest --browser firefox
```

- full_test. The user can choose between full test or reduced test mode. Reduced is the default option, to avoid restriction due the number of web requests. Example for full test mode:
```bash
pytest --full_test True
```

The user can combine both arguments as:
```bash
pytest --browser edge --full_test False
```

- headless and disable-dev-shm-usage arguments are meant to allow the execution of this test strategy in a CI environment by a GitHub workflow. In this cases, headless and disable-dev-shm-usage will be set to True. False, otherwise and by default.

## Test results

pytest will provide a test execution summary in the terminal

# TEST AUTOMATION 
To automate the execution of this test strategy when code is pushed to the repository, a file python-ci_exercise_2.yml has been added to .github/workflows in order to define a workflow in GitHub. 
This workflow triggers on every push to the main branch. It checks out the code, sets up Python, installs project dependencies, and runs tests using pytest.
After the workflow completes, you can view test results and logs directly in the Actions tab in GitHub. If there are any test failures, you'll be notified.

A html report gets uploaded as an artifact accessible in GitHub