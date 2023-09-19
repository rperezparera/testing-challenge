"""
File: json_utils.py
Description: This file contains json comparison methods
Author: Roger Pérez Parera
Date: 20th September, 2023
"""
from jsondiff import diff

# ===========================
# == JSON COMPARISON UTILS ==
# ===========================
 #Function to compare two JSON objects and check if they are equal
def compare_json(json1, json2):
    json_diff = diff(json1, json2)
    if not json_diff:
        return True
    return False

# Function to compare two lists of books (represented as JSON objects)
def compare_list_books(book_list1, book_list2):
    # Check if the lengths of both lists are equal
    if not len(book_list1) == len(book_list2):
        return False
    
    # Iterate through the lists and compare each book using compare_json
    for i in range(0, len(book_list1)):
        if not compare_json(book_list1[i], book_list2[i]):
            return False
    
    return True