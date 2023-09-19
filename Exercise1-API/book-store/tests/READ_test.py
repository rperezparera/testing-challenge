"""
File: READ_test.py
Description: This file contains test cases for retrieving books from bookstore_api
             The tests include retrieving all books and retrieving a single book.
Author: Roger Pérez Parera
Date: 20th September, 2023
"""
from test_utils import constants, json_utils, utils
import json
import pytest

# ===========================
# ======= TEST DATA =========
# ===========================
# Test data for retrieving all books
test_data_retrieve_all = [
    # Test Case 1: Retrieve all, empty store
    # Expected response: Created books to retrieved books
    ([], ""),

    # Test Case 2: Retrieve all, one book store
    # Expected response: Created books to retrieved books
    ([constants.book1], constants.expected_retrieve_1),

    # Test Case 3: Retrieve all, two book store
    # Expected response: Created books to retrieved books
    ([constants.book1, constants.book2], constants.expected_retrieve_2),

    # Test Case 4: Retrieve all, 4 book store
    # Expected response: Created books to retrieved books
    ([constants.book1, constants.book2, constants.book3, constants.book4], constants.expected_retrieve_3),

    # Test Case 5: Retrieve all, 10 book store
    # Expected response: Created books to retrieved books
    ([constants.book1, constants.book2, constants.book3, constants.book4, constants.book5,constants.book6, constants.book7,
       constants.book8, constants.book9, constants.book10], constants.expected_retrieve_4),
]

# Test data for retrieving a single book
test_data_retrieve_single = [
    # Test Case 1: Retrieve a single not existing book
    # Expected response: 404 status code, book not found
    ([], "1", constants.error_book_not_found, 404),

    # Test Case 2: Retrieve a single not existing book (extended)
    # Expected response: 404 status code, book not found
    ([], "abc", constants.error_book_not_found, 404),

    # Test Case 3: Retrieve a single book that exists
    # Expected response: 200 status code, book found
    ([constants.book1], "1", constants.expected_retrieve_single_1, 200),

    # Test Case 4: Retrieve a single book that exists, after adding two
    # Expected response: 200 status code, book found
    ([constants.book1, constants.book2], "1", constants.expected_retrieve_single_1, 200),

    # Test Case 5: Retrieve a single book that exists, after adding ten
    # Expected response: 200 status code, book found
    ([constants.book1, constants.book2, constants.book3, constants.book4, constants.book5, constants.book6, constants.book7,
       constants.book8, constants.book9, constants.book10], "1", constants.expected_retrieve_single_1, 200),

    # Test Case 5: Retrieve a single book that exists, after adding ten (extended)
    # Expected response: 200 status code, book found
    ([constants.book1, constants.book2, constants.book3, constants.book4, constants.book5, constants.book6, constants.book7,
       constants.book8, constants.book9, constants.book10], "9", constants.expected_retrieve_single_2, 200)
]

# ===========================
# ====== RETRIEVE ALL =======
# ======= TEST CASE =========
# ===========================
# Test processing for retrieving all books
@pytest.mark.parametrize("books_to_create, expected_response", test_data_retrieve_all)
def test_case_retrieve_all_operation(books_to_create, expected_response):
    utils.preprocessing()

    create_and_retrieve_all_books_and_validate(books_to_create, expected_response)
    
    utils.postprocessing()

# ===========================
# ===== RETRIEVE SINGLE =====
# ======= TEST CASES ========
# ===========================
# Test processing for retrieving all books
@pytest.mark.parametrize("books_to_create, book_id, expected_response, expected_status_code", test_data_retrieve_single)
def test_case_retrieve_single_operation(books_to_create, book_id, expected_response, expected_status_code):
    utils.preprocessing()

    create_and_retrieve_single_book_and_validate(books_to_create, book_id, expected_response, expected_status_code)
    
    utils.postprocessing() 

# ===========================
# ===== TEST FUNCTIONS ======
# ===========================
# Function to create and retrieve all books and validate the results
def create_and_retrieve_all_books_and_validate(books_list, expected_retrieved):
    # Create books
    for book in books_list:
        utils.create_book(book)

    # Retrieve book
    response = utils.retrieve_all_books()
    
    # Validate correct HTTP status code
    assert utils.get_status_code(response) == 200

    # Validate response payload
    if expected_retrieved:
        with open(expected_retrieved) as file:
            book_list = json.load(file)
            assert json_utils.compare_list_books(utils.get_response_payload(response), book_list)

    # Validate response headers
    assert utils.get_response_header(response) == "application/json"

# Function to create and retrieve a single book and validate the results
def create_and_retrieve_single_book_and_validate(books_list, book_id, expected_retrieved, expected_status_code):
    # Create books
    if books_list != []:
        for book in books_list:
            utils.create_book(book)

    # Retrieve book
    response = utils.retrieve_single_book(book_id)
    
    # Validate correct HTTP status code
    assert utils.get_status_code(response) == expected_status_code

    # Validate response payload
    if expected_retrieved:
        with open(expected_retrieved) as file:
            assert json_utils.compare_json(utils.get_response_payload(response), json.load(file))

    # Validate response headers
    assert utils.get_response_header(response) == "application/json"    