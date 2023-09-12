# Unit Testing Challenge - Exercise 1: Book Store REST API

## Objective

The main objective of this challenge is to create comprehensive and robust unit tests for a RESTful API. The challenge aims to assess your understanding of REST API testing principles, including the HTTP protocol, CRUD operations, and various testing strategies such as boundary conditions, data-driven testing, and validation of responses.

## Challenge Description

You will be provided with a REST API that performs CRUD (Create, Read, Update, Delete) operations for a bookstore. The API has the following endpoints:

1. `POST /books` - Create a new book
2. `GET /books` - Retrieve a list of all books
3. `GET /books/{book_id}` - Retrieve details of a single book
4. `PUT /books/{book_id}` - Update a book's details
5. `DELETE /books/{book_id}` - Delete a book

### API Schema for Book

```json
{
  "book_id": "string",
  "title": "string",
  "author": "string",
  "published_date": "YYYY-MM-DD",
  "isbn": "string",
  "price": "float"
}

```

### Challenge Requirements

1. **Setup**
Clone the given API repository and follow the README instructions to set it up locally.
2. **Testing Framework**
Use pytest as testing framework for Python.
3. **Test Scenarios**
    - Write test cases for each of the CRUD operations.
        1. Validate correct HTTP status codes.
        2. Validate response payload.
        3. Validate response headers.
        4. Validate fault conditions (e.g., what happens if you try to read a book that does not exist?).
    - Implement boundary tests (e.g., very long strings, negative numbers).
    - Implement data-driven tests with multiple sets of data.
4. **Documentation**
    - Modify the README file to contains:
        1. An explanation of your testing strategy.
        2. Instructions on how to run the tests.
5. **Bonus: Automation**
Create a CI/CD pipeline that runs your tests automatically when code is pushed to the repository.

### Deliverables

A GitHub repository containing:
    1. All your test scripts.
    2. A README file explaining your testing strategy and how to run the tests.
    3. (Optional) CI/CD configuration files.

### Evaluation Criteria

- **Completeness**: All CRUD operations should be covered.
- **Robustness**: Tests should handle both happy and unhappy paths.
- **Documentation**: Clear documentation explaining the strategy and how to run the tests.
- **Code Quality**: Code should be clean, well-organized, and follow best practices.

Feel free to adjust the challenge according to your specific needs.

## How to run the API

```bash
python bookstore_api.py

```

Your API will start running at **`http://127.0.0.1:5000/`**.

### **API Endpoints:**

- **Create a New Book**: POST request to **`http://127.0.0.1:5000/books`**
- **Retrieve All Books**: GET request to **`http://127.0.0.1:5000/books`**
- **Retrieve a Single Book**: GET request to **`http://127.0.0.1:5000/books/{book_id}`**
- **Update a Book**: PUT request to **`http://127.0.0.1:5000/books/{book_id}`**
- **Delete a Book**: DELETE request to **`http://127.0.0.1:5000/books/{book_id}`**

You can modify the code to add more complexity if desired. After completing the API, testers can begin creating unit tests for these endpoints following the challenge guidelines.
