"""
File: DELETE_test.py
Description: Test cases for DELETE operation in bookstore_api 
             It includes scenarios for deleting single and multiple books.
             Test data is provided to cover various deletion scenarios.
Author: Roger Pérez Parera
Date: 20th September, 2023
"""
from test_utils import constants, json_utils, utils
import json
import pytest

# ===========================
# ======= TEST DATA ========
# ===========================
test_data = [
    # Test Case 1: Delete a single book successfully
    # Expected response: 204 status code, succesful operation
    ([constants.book1], ["1"], constants.succesful_deletion, 204),

    # Test Case 2: Delete a non-existing book
    # Expected response: 404 status code, book not found
    ("", ["1"], constants.error_book_not_found, 404),

    # Test Case 3: Delete multiple books successfully
    # Expected response: 204 status code, succesful operation in each deletion
    ([constants.book1, constants.book2, constants.book3], ["1", "2", "3"], constants.succesful_deletion, 204),

    # Test Case 4: Delete multiple books successfully (extended)
    # Expected response: 204 status code, succesful operation in each deletions
    ([constants.book1, constants.book2, constants.book3, constants.book4, constants.book5, constants.book6], 
     ["1", "2", "3", "4", "5", "6"], constants.succesful_deletion, 204),
]

# ===========================
# ======= TEST CASES ========
# ===========================
# Parameterized test case function that runs with different deletion scenarios
@pytest.mark.parametrize("books_to_create, book_id_list, expected_response, expected_status_code", test_data)
def test_case_delete_operation(books_to_create, book_id_list, expected_response, expected_status_code):
    utils.preprocessing()

    for book in books_to_create:
        utils.create_book(book)

    delete_books_and_validate(book_id_list, expected_response, expected_status_code)

    utils.postprocessing()

# ===========================
# ===== TEST FUNCTIONS ======
# ===========================
# Perform book deletion for a list of book IDs and validate the API response.
def delete_books_and_validate(book_id_list, expected_response, expected_status_code):

    # Iterate over the list of book IDs to be deleted
    for id in book_id_list:
        # Delete
        response = utils.delete_book(id)

        # Validate correct HTTP status code
        status_code = utils.get_status_code(response)
        if expected_status_code != "": assert status_code == expected_status_code

        # Validate response payload
        if not status_code == 204:
            with open(expected_response) as file:
                assert json_utils.compare_json(utils.get_response_payload(response), json.load(file))

        # Validate response headers
        assert utils.get_response_header(response) == "application/json"

    