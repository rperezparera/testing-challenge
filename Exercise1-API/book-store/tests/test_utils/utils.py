"""
File: utils.py
Description: This file contains utility functions for performing CRUD operations on bookstore_api,
             as well as methods for parsing API responses and preprocessing/postprocessing tasks.
Author: Roger Pérez Parera
Date: 20th September, 2023
"""
import requests
import json

# ===========================
# URL to make the POST request
# ===========================
url = "http://127.0.0.1:5000/"

# ===========================
# ===== CRUD OPERATIONS =====
# ===========================
# Function to create a book by sending a POST request with JSON data
def create_book(jsonFile):
    with open(jsonFile) as file:
        raw_json = json.load(file)
        response = requests.post(url + 'books', data=json.dumps(raw_json), headers={"Content-Type": "application/json"})
        return response

# Function to create a book by sending a POST request with JSON data
def retrieve_all_books():
    response = requests.get(url + 'books')
    return response

# Function to retrieve a single book by sending a GET request with the book ID
def retrieve_single_book(book):
    response = requests.get(url + 'books/' + book)
    return response

# Function to retrieve a single book by sending a GET request with the book ID
def update_book(book, jsonFile):
    with open(jsonFile) as file:
        raw_json = json.load(file)
        response = requests.put(url + 'books/' + book, data=json.dumps(raw_json), headers={"Content-Type": "application/json"})
        return response

# Function to delete a book by sending a DELETE request with the book ID
def delete_book(book):
    response = requests.delete(url + 'books/' + book)
    return response

# ===========================
# ===== RESPONSE PARSER =====
# ===========================
# Function to get the HTTP status code from a response
def get_status_code(response):
    return response.status_code

# Function to get the JSON payload from a response
def get_response_payload(response):
    return response.json()

# Function to get the Content-Type header from a response
def get_response_header(response):
    return response.headers.get("Content-Type")

# ===========================
# === PREPROCESSING METHOD ==
# ===========================
# Function to perform preprocessing tasks (remove all books in the store)
def preprocessing():
    delete_all_books()

# ===========================
# == POSTPROCESSING METHOD ==
# ===========================
# Function to perform preprocessing tasks (remove all books in the store)
def postprocessing():
    delete_all_books()

# ===========================
# === OTHER UTILS METHODS ===
# ===========================
# Function to delete all books in the store
def delete_all_books():
    data = get_response_payload(retrieve_all_books())
    books_ids = []
    for item in data:
        book_id = item["book_id"]
        books_ids.append(book_id)

    for id in books_ids:
        delete_book(id)