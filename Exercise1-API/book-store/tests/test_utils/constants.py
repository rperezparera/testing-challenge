"""
File: constants.py
Description: This file contains json file routes used in the tests.
Author: Roger Pérez Parera
Date: 20th September, 2023
"""
# ===========================
# ======== CONSTANTS ========
# ===========================
# Directory path for sample JSON files
sample_dir = "samples/"

# Sample JSON files for valid books
book1 = sample_dir + "valid_data_book.json"
book2 = sample_dir + "valid_data_book2.json"
book3 = sample_dir + "valid_data_book3.json"
book4 = sample_dir + "valid_data_book4.json"
book5 = sample_dir + "valid_data_book5.json"
book6 = sample_dir + "valid_data_book6.json"
book7 = sample_dir + "valid_data_book6.json"
book8 = sample_dir + "valid_data_book8.json"
book9 = sample_dir + "valid_data_book9.json"
book10 = sample_dir + "valid_data_book10.json"

# Sample JSON files for missing required fields
missing_field_title_book = sample_dir + "missing_field_title_book.json"
missing_field_author_book = sample_dir + "missing_field_author_book.json"
missing_field_date_book = sample_dir + "missing_field_date_book.json"
missing_field_isbn_book = sample_dir + "missing_field_isbn_book.json"
missing_field_price_book = sample_dir + "missing_field_price_book.json"

# Sample JSON files for error responses
boundary_1 = sample_dir + "boundary_1.json"
boundary_2 = sample_dir + "boundary_2.json"
boundary_3 = sample_dir + "boundary_3.json"
boundary_4 = sample_dir + "boundary_4.json"
boundary_5 = sample_dir + "boundary_5.json"
boundary_6 = sample_dir + "boundary_6.json"
boundary_7 = sample_dir + "boundary_7.json"
boundary_8 = sample_dir + "boundary_8.json"
boundary_9 = sample_dir + "boundary_9.json"
boundary_10 = sample_dir + "boundary_10.json"
boundary_11 = sample_dir + "boundary_11.json"
boundary_12 = sample_dir + "boundary_12.json"
boundary_13 = sample_dir + "boundary_13.json"
boundary_14 = sample_dir + "boundary_14.json"
boundary_15 = sample_dir + "boundary_15.json"

# Sample JSON files for missing required fields
expected_1 = sample_dir + "expected1.json"
expected_2 = sample_dir + "expected2.json"
expected_3 = sample_dir + "expected3.json"
expected_4 = sample_dir + "expected4.json"
expected_5 = sample_dir + "expected5.json"
expected_6 = sample_dir + "expected6.json"
expected_7 = sample_dir + "expected7.json"
expected_8 = sample_dir + "expected8.json"
expected_9 = sample_dir + "expected9.json"
expected_10 = sample_dir + "expected10.json"
expected_retrieve_1 = sample_dir + "expected_retrieve_1.json"
expected_retrieve_2 = sample_dir + "expected_retrieve_2.json"
expected_retrieve_3 = sample_dir + "expected_retrieve_3.json"
expected_retrieve_4 = sample_dir + "expected_retrieve_4.json"
expected_retrieve_single_1 = sample_dir + "expected_retrieve_single_1.json"
expected_retrieve_single_2 = sample_dir + "expected_retrieve_single_2.json"
expected_boundary_1 = sample_dir + "expected_boundary_1.json"
expected_boundary_3 = sample_dir + "expected_boundary_3.json"
expected_boundary_4 = sample_dir + "expected_boundary_4.json"
expected_boundary_10 = sample_dir + "expected_boundary_10.json"
expected_boundary_15 = sample_dir + "expected_boundary_15.json"

# Sample JSON files for updated books and expected responses
updated_book_1 = sample_dir + "updated_book_1.json"
updated_expected_1 = sample_dir + "updated_expected_1.json"
updated_expected_2 = sample_dir + "updated_expected_2.json"
updated_book_invalid = sample_dir + "updated_book_invalid.json"

# Sample JSON files for successful deletion response
succesful_deletion = sample_dir + "succesful_deletion.json"

# Sample JSON files for error responses
error_book_not_found = sample_dir + "error_book_not_found.json"
error_missing_required_fields = sample_dir + "error_missing_required_fields.json"
error_invalid_date = sample_dir + "error_invalid_date.json"
error_empty_title = sample_dir + "error_empty_title.json"
error_invalid_isbn = sample_dir + "error_invalid_isbn.json"
error_invalid_price = sample_dir + "error_invalid_price.json"

# Sample JSON file for an empty book
empty_book = sample_dir + "empty_book.json"

# Sample JSON file for a book with up-to-date information
book_up_to_date = sample_dir + "book_up_to_date.json"
