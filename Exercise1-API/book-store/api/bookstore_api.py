from flask import Flask, request, jsonify, make_response
from datetime import datetime
import re

app = Flask(__name__)

# In-memory database
books = []

def find_book(book_id):
    return next((book for book in books if book['book_id'] == book_id), None)

# Function to validate a book's date
def validate_date(date):
    # Accepted formats
    for date_format in ["%Y-%m-%d", "%d-%m-%Y", "%Y", "%b %d, %Y", "%B %d, %Y", "%B %Y"]:
        try:
            parsed_date = datetime.strptime(date, date_format)
            break  # If successful
        except ValueError:
            pass
    else:
        return False
    current_date = datetime.now()
    if parsed_date > current_date: return False # Reject future dates
    return True

# Function to validate a book's ISBN
def validate_isbn(isbn):
    # Clear the input ISBN from hyphens or spaces 
    isbn = re.sub(r'[-\s]', '', isbn)
    
    # Check if it could be a valid ISBN-10 or ISBN-13
    if not (len(isbn) == 10 and isbn.isdigit()) and not (len(isbn) == 13 and isbn.isdigit()):
       return False
    return True  

# Function to validate a book's price
def validate_price(price):
    # Reject empty price
    if not price: return False
    
    if isinstance(price, str):
        # Reject not numeric prices
        if not price.isdigit(): return False
        number = float(price)
    else:
        number = price

    # Reject negative prices
    if number < 0:
        return False
    else:
        return True

# Function to validate a specific field on a set of data
def validate_field(field, data):
    if field == 'title':
        if not data['title']:
            return make_response(
                jsonify({'error': 'Empty title'}), 400)
    elif field == 'published_date':
        if not validate_date(data['published_date']): 
            return make_response(
                jsonify({'error': 'Invalid date'}), 400)
    elif field == 'isbn':
        if not validate_isbn(data['isbn']):
            return make_response(
                jsonify({'error': 'Invalid isbn'}), 400)
    elif field == 'price':
        if not validate_price(data['price']):
            return make_response(
                jsonify({'error': 'Invalid price'}), 400)
    return 

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()

    required_fields = ['title', 'author', 'published_date', 'isbn', 'price']
    if not all(field in data for field in required_fields):
        return make_response(
            jsonify({'error': 'Missing required fields'}), 400)
        
    # validate fields using validate_field method
    for field in ['title', 'published_date', 'isbn', 'price']:
        validation = validate_field(field, data)
        if validation: return validation
    
    new_book = {
        'book_id': str(len(books) + 1),
        'title': data['title'],
        'author': data['author'],
        'published_date': data['published_date'],
        'isbn': data['isbn'],
        'price': data['price']
    }

    books.append(new_book)
    return make_response(jsonify(new_book), 201)


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


@app.route('/books/<string:book_id>', methods=['GET'])
def get_single_book(book_id):
    book = find_book(book_id)
    if book is None:
        return make_response(jsonify({'error': 'Book not found'}), 404)
    return jsonify(book)


@app.route('/books/<string:book_id>', methods=['PUT'])
def update_book(book_id):
    book = find_book(book_id)
    if book is None:
        return make_response(jsonify({'error': 'Book not found'}), 404)

    data = request.get_json()

    for field in ['title', 'author', 'published_date', 'isbn', 'price']:
        if field in data:
            # validate each field using validate_field method
            validation = validate_field(field, data)
            if validation: return validation
            book[field] = data[field]
    return jsonify(book)


@app.route('/books/<string:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = find_book(book_id)
    if book is None:
        return make_response(jsonify({'error': 'Book not found'}), 404)

    books.remove(book)
    return make_response(jsonify({'message': 'Book deleted successfully'}), 204)


if __name__ == '__main__':
    app.run(debug=True)
