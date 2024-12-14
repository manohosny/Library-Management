"""Test suite for Library Management System API."""
import pytest
from app import app

@pytest.fixture
def test_client():
    """Configure test client fixture."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_book(test_client):
    """Test adding a new book."""
    book = {
        "title": "Test Book",
        "author": "Test Author",
        "published_year": 2023,
        "isbn": "123-4567890"
    }
    response = test_client.post('/books', json=book)
    assert response.status_code == 201
    assert response.json['title'] == book['title']

def test_add_book_missing_fields(test_client):
    """Test adding a book with missing required fields."""
    book = {"title": "Test Book"}
    response = test_client.post('/books', json=book)
    assert response.status_code == 400

def test_list_books(test_client):
    """Test retrieving all books."""
    response = test_client.get('/books')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_search_books_by_author(test_client):
    """Test searching books by author."""
    book = {
        "title": "Search Test",
        "author": "Search Author",
        "published_year": 2023,
        "isbn": "999-8887776"
    }
    test_client.post('/books', json=book)
    
    response = test_client.get('/books/search?author=Search Author')
    assert response.status_code == 200
    assert len(response.json) > 0
    assert response.json[0]['author'] == 'Search Author'

def test_delete_book(test_client):
    """Test deleting a book."""
    book = {
        "title": "Delete Test",
        "author": "Delete Author",
        "published_year": 2023,
        "isbn": "777-6665554"
    }
    test_client.post('/books', json=book)
    
    response = test_client.delete(f'/books/{book["isbn"]}')
    assert response.status_code == 204

def test_update_book(test_client):
    """Test updating a book."""
    book = {
        "title": "Update Test",
        "author": "Update Author",
        "published_year": 2023,
        "isbn": "444-3332221"
    }
    test_client.post('/books', json=book)
    
    update_data = {
        "title": "Updated Title",
        "published_year": 2024
    }
    response = test_client.put(f'/books/{book["isbn"]}', json=update_data)
    assert response.status_code == 200
    assert response.json['title'] == "Updated Title"
    assert response.json['published_year'] == 2024