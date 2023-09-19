"""
File: CREATE_test.py
Description: Test cases for CREATE operation in bookstore_api. 
             It includes various test scenarios with different data inputs and expected outcomes.
             Test data is organized into a list of dictionaries, with each dictionary representing a test case.
             Each test case includes books to create, the expected API response, and the expected HTTP status code.
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
    # Test Case 1: Create 1 book with valid data
    # Expected response: 201 status code, succesful operation
    ([constants.book1], [constants.expected_1], 201),

    # Test Case 2: Create 2 books with valid data
    # Expected response: 201 status code, succesful operation
    ([constants.book1, constants.book2], [constants.expected_1, constants.expected_2], 201),

    # Test Case 3: Create 4 books with valid data
    # Expected response: 201 status code, succesful operation
    ([constants.book1, constants.book2, constants.book3, constants.book4],
     [constants.expected_1, constants.expected_2, constants.expected_3, constants.expected_4], 201),

    # Test Case 4: Create 10 books with valid data
    # Expected response: 201 status code, succesful operation
    ([constants.book1, constants.book2, constants.book3, constants.book4, constants.book5,
      constants.book6, constants.book7, constants.book8, constants.book9, constants.book10],
     [constants.expected_1, constants.expected_2, constants.expected_3, constants.expected_4, constants.expected_5,
      constants.expected_6, constants.expected_7, constants.expected_8, constants.expected_9, constants.expected_10], 201),

    # Test Case 5: Create a book with title missing field
    # Expected response: 400 status code, the API rejects the creation when this field is missing
    ([constants.missing_field_title_book], [constants.error_missing_required_fields], 400),

    # Test Case 6: Create a book with author missing field
    # Expected response: 400 status code, the API rejects the creation when this field is missing
    ([constants.missing_field_author_book], [constants.error_missing_required_fields], 400),

    # Test Case 7: Create a book with date missing field
    # Expected response: 400 status code, the API rejects the creation when this field is missing
    ([constants.missing_field_date_book], [constants.error_missing_required_fields], 400),

    # Test Case 8: Create a book with isbn missing field
    # Expected response: 400 status code, the API rejects the creation when this field is missing
    ([constants.missing_field_isbn_book], [constants.error_missing_required_fields], 400),

    # Test Case 9: Create a book with price missing field
    # Expected response: 400 status code, the API rejects the creation when this field is missing
    ([constants.missing_field_price_book], [constants.error_missing_required_fields], 400),

    # Test Case 10: Create a book with empty data
    # Expected response: 400 status code, the API rejects the creation when missing all the fields
    ([constants.empty_book], [constants.error_missing_required_fields], 400),

    # Boundary Test Case 1: Create with a 500-character title
    # Expected response: 201 status code, succesful operation
    ([constants.boundary_1], [constants.expected_boundary_1], 201),

    # Boundary Test Case 2: Create with an empty title
    # Expected response: 201 status code, not allowed
    ([constants.boundary_2], [constants.error_empty_title], 400),

    # Boundary Test Case 3: Create with a 500-character author
    # Expected response: 201 status code, succesful operation
    ([constants.boundary_3], [constants.expected_boundary_3], 201),

    # Boundary Test Case 4: Create with an empty author
    # Expected response: 201 status code, succesful operation (anonymous cases)
    ([constants.boundary_4], [constants.expected_boundary_4], 201),

    # Boundary Test Case 5: Create with a future date
    # Expected response: 400 status code, API rejects dates after today's date
    ([constants.boundary_5], [constants.error_invalid_date], 400),

    # Boundary Test Case 6: Create with an empty date
    # Expected response: 400 status code, API rejects empty dates
    ([constants.boundary_6], [constants.error_invalid_date], 400),

    # Boundary Test Case 7: Create with an invalid date format
    # Expected response: 400 status code, API only accepts valid date formats
    ([constants.boundary_7], [constants.error_invalid_date], 400),

    # Boundary Test Case 8: Create with a 500-character ISBN
    # Expected response: 400 status code, API checks isbn satisfies the preliminary conditions to be isbn-10 or 13
    ([constants.boundary_8], [constants.error_invalid_isbn], 400),

    # Boundary Test Case 9: Create with an empty ISBN
    # Expected response: 400 status code, API requires an ISBN
    ([constants.boundary_9], [constants.error_invalid_isbn], 400),

    # Boundary Test Case 10: Create with a 500-character price
    # Expected response: 201 status code, succesful operation
    ([constants.boundary_10], [constants.expected_boundary_10], 201),

    # Boundary Test Case 11: Create with an empty price
    # Expected response: 400 status code, API requires a price
    ([constants.boundary_11], [constants.error_invalid_price], 400),

    # Boundary Test Case 12: Create with a negative price
    # Expected response: 400 status code, API rejects not correct prices
    ([constants.boundary_12], [constants.error_invalid_price], 400),

    # Boundary Test Case 13: Create with a price containing letters
    # Expected response: 400 status code, API rejects not correct prices
    ([constants.boundary_13], [constants.error_invalid_price], 400),

    # Boundary Test Case 14: Create with a price containing special characters
    # Expected response: 400 status code, API rejects not correct prices
    ([constants.boundary_14], [constants.error_invalid_price], 400),

    # Boundary Test Case 15: Create with an additional unrecognized key
    # Expected response: 201 status code, API ignores additional keys/fields
    ([constants.boundary_15], [constants.expected_boundary_15], 201),
]

# ===========================
# ======= TEST CASES ========
# ===========================
# Parameterized test case function that creates and validates books with various data combinations
@pytest.mark.parametrize("books_to_create, expected_response, expected_status_code", test_data)
def test_case_create_operation(books_to_create, expected_response, expected_status_code):
    utils.preprocessing()

    create_books_and_validate(books_to_create, expected_response, expected_status_code)

    utils.postprocessing()

# ===========================
# ===== TEST FUNCTIONS ======
# ===========================
# Function to create books, validate HTTP status codes, response payloads, and headers
def create_books_and_validate(books_list, expected_list, expected_SW):
    if not len(books_list) == len(expected_list):
        # Incorrect parameters
        pytest.xfail("This test encountered a fatal error. Book list and expected list do not have the same length")
    
    for i in range(0, len(books_list)):

        # Create books
        response = utils.create_book(books_list[i])
    
        # Validate correct HTTP status code
        assert utils.get_status_code(response) == expected_SW

        # Validate response payload
        with open(expected_list[i]) as file:
            assert json_utils.compare_json(utils.get_response_payload(response), json.load(file))

        # Validate response headers
        assert utils.get_response_header(response) == "application/json"