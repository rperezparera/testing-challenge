"""
File: random_book.py
Description: This file provides utility functions for generating random book data and ISBN-13 numbers,
             as well as making requests to the Open Library API to retrieve book information.
Author: Roger Pérez Parera
Date: 20th September, 2023
"""
from test_utils import constants
import requests
import random
import json

# Function to provide random book data by making a request to the Open Library API
def provide_random_book_data(): 
    random_number = random.randint(1, 36475544)

    # Construct an OLID based on the random number
    random_olid = f"OL{random_number}M"

    # Define the Open Library API endpoint 
    base_url = f"https://openlibrary.org/api/books"

    params = {
        "bibkeys": f"OLID:{random_olid}",
        "format": "json",
        "jscmd": "data",
    }

    # Make the GET request to the API
    response = requests.get(base_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        book_info = response.json().get(f"OLID:{random_olid}", {})

        # Extract the title and author information
        title = book_info.get("title", "Title not available")
        authors = book_info.get("authors", [{"name": "Idoven"}])
        published_date = book_info.get("publish_date", "1996")
        isbn_10 = book_info.get("isbn_10", "")
        isbn_13 = book_info.get("isbn_13", "")
        isbn = generate_random_isbn_13() if not any([isbn_10, isbn_13]) else isbn_10 or isbn_13

        book_data = {
            "title": title,
            "author": [author["name"] for author in authors],
            "isbn": isbn,
            "price": generate_random_price(),
            "published_date": published_date,
            "book_id": "1",
        }
        book_json = json.dumps(book_data, indent=4)
        filename = constants.sample_dir + "temp_book.json"

        with open(filename, "w") as json_file:
            json_file.write(book_json)

        return filename
    else:
        print("Error:", response.status_code)

# Function to generate a random ISBN-13 number
def generate_random_isbn_13():
    # Generate a random number for the title identifier part (9 digits)
    title_identifier = ''.join(random.choice('0123456789') for _ in range(9))

    # Create the first 12 digits of the ISBN
    isbn_prefix = '978'  # Prefix for ISBN-13
    partial_isbn = isbn_prefix + title_identifier

    # Calculate the ISBN-13 checksum
    checksum = 0
    for i, digit in enumerate(partial_isbn):
        if i % 2 == 0:
            checksum += int(digit)
        else:
            checksum += 3 * int(digit)
    checksum = (10 - (checksum % 10)) % 10

    # Combine all
    isbn_13 = partial_isbn + str(checksum)

    return isbn_13

# Function to generate a random price for a book
def generate_random_price():
    # Generate a random floating-point number between 0.01 and 199
    return round(random.uniform(0.01, 199), 2)