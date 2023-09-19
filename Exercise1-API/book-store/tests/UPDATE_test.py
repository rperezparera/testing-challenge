"""
File: UPDATE_test.py
Description: Test cases for UPDATE operation in bookstore_api. 
             It includes various test scenarios with different data inputs and expected outcomes.
             Test data is organized into a list of dictionaries, with each dictionary representing a test case.
             Each test case includes books to create, book ID to update, update data, the expected API response, and the expected HTTP status code.
Author: Roger Pérez Parera
Date: 20th September, 2023
"""

from test_utils import constants, json_utils, utils
import json
import pytest

# ===========================
# ======= TEST DATA =========
# ===========================
test_data = [
    # Test Case 1: Update an existing book with valid data
    # Expected response: 200 status code, succesful operation
    ([constants.book1], "1", constants.updated_book_1, constants.updated_expected_1, 200),

    # Test Case 2: Update an existing book in a 10 book store
    # Expected response: 200 status code, succesful operation
    ([constants.book1, constants.book2, constants.book3, constants.book4, constants.book5, constants.book6, constants.book7,
      constants.book8, constants.book9, constants.book10], "5", constants.updated_book_1, constants.updated_expected_2, 200),

    # Test Case 3: Update an existing book with invalid data
    # Expected response: 200 status code, succesful operation. API only updates valid data, ignores the rest.
    ([constants.book1], "1", constants.updated_book_invalid, constants.expected_1, 200),

    # Test Case 4: Update a non-existing book
    # Expected response: 404 status code, book not found
    ([constants.book1], "2", constants.updated_book_1, constants.error_book_not_found, 404),

    # Test Case 5: Update an empty book
    # Expected response: 404 status code, book not found
    ([constants.empty_book], "1", constants.updated_book_1, constants.error_book_not_found, 404),

    # Boundary Test Case 1: Update with a 500-character title
    # Expected response: 200 status code, succesful operation
    ([constants.book1], "1", constants.boundary_1, constants.expected_boundary_1, 200),

    # Boundary Test Case 2: Update with an empty title
    # Expected response: 400 status code, API rejects to update to a empty title
    ([constants.book1], "1", constants.boundary_2, constants.error_empty_title, 400),

    # Boundary Test Case 3: Update with a 500-character author
    # Expected response: 200 status code, succesful operation
    ([constants.book1], "1", constants.boundary_3, constants.expected_boundary_3, 200),

    # Boundary Test Case 4: Update with an empty author
    # Expected response: 200 status code, succesful operation (anonymous case)
    ([constants.book1], "1", constants.boundary_4, constants.expected_boundary_4, 200),

    # Boundary Test Case 5: Update with a future date
    # Expected response: 400 status code, API rejects to update to an invalid date
    ([constants.book1], "1", constants.boundary_5, constants.error_invalid_date, 400),

    # Boundary Test Case 6: Update with an empty date
    # Expected response: 400 status code, API rejects to update to an invalid date
    ([constants.book1], "1", constants.boundary_6, constants.error_invalid_date, 400),

    # Boundary Test Case 7: Update with an invalid date format
    # Expected response: 400 status code, API rejects to update to an invalid date
    ([constants.book1], "1", constants.boundary_7, constants.error_invalid_date, 400),

    # Boundary Test Case 8: Update with a 500-character ISBN
    # Expected response: 400 status code, API rejects to update to an invalid isbn
    ([constants.book1], "1", constants.boundary_8, constants.error_invalid_isbn, 400),

    # Boundary Test Case 9: Update with an empty ISBN
    # Expected response: 400 status code, API rejects to update to an invalid isbn
    ([constants.book1], "1", constants.boundary_9, constants.error_invalid_isbn, 400),

    # Boundary Test Case 10: Update with a 500-character price
    # Expected response: 200 status code, succesful operation
    ([constants.book1], "1", constants.boundary_10, constants.expected_boundary_10, 200),

    # Boundary Test Case 11: Update with an empty price
    # Expected response: 400 status code, API rejects to update to an invalid price
    ([constants.book1], "1", constants.boundary_11, constants.error_invalid_price, 400),

    # Boundary Test Case 12: Update with a negative price
    # Expected response: 400 status code, API rejects to update to an invalid price
    ([constants.book1], "1", constants.boundary_12, constants.error_invalid_price, 400),

    # Boundary Test Case 13: Update with a price containing letters
    # Expected response: 400 status code, API rejects to update to an invalid price
    ([constants.book1], "1", constants.boundary_13, constants.error_invalid_price, 400),

    # Boundary Test Case 14: Update with a price containing special characters
    # Expected response: 400 status code, API rejects to update to an invalid price
    ([constants.book1], "1", constants.boundary_14, constants.error_invalid_price, 400),
]

# Parameterized test case function that creates, updates and validates various data combinations
@pytest.mark.parametrize("books_to_create, book_id, update_book, expected_response, expected_status_code", test_data)
def test_case_update_operation(books_to_create, book_id, update_book, expected_response, expected_status_code):
    utils.preprocessing()

    # Create books
    for book in books_to_create:
        utils.create_book(book)

    update_book_and_validate(book_id, update_book, expected_response, expected_status_code)

    utils.postprocessing()

# ===========================
# ===== TEST FUNCTIONS ======
# ===========================
# Function to update books and validate HTTP status codes, response payloads, and headers
def update_book_and_validate(book_id, update_book, expected_response, expected_status_code):

    # Update book
    response = utils.update_book(book_id, update_book)

    # Validate correct HTTP status code
    assert utils.get_status_code(response) == expected_status_code

    # Validate response payload
    with open(expected_response) as file:
        assert json_utils.compare_json(utils.get_response_payload(response), json.load(file))

    # Validate response headers
    assert utils.get_response_header(response) == "application/json"    