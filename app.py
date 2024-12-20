"""Library Management System API implementation."""
from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

books = []

SWAGGER_URL = '/api-docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Library Management System API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/books', methods=['POST'])
def add_book():
    """Add a new book to the library."""
    data = request.json
    required_fields = ['title', 'author', 'published_year', 'isbn']
    
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    for book in books:
        if book['isbn'] == data['isbn']:
            return jsonify({'error': 'Book with this ISBN already exists'}), 409
    
    book = {
        'title': data['title'],
        'author': data['author'],
        'published_year': data['published_year'],
        'isbn': data['isbn'],
        'genre': data.get('genre')
    }
    books.append(book)
    return jsonify(book), 201

@app.route('/books', methods=['GET'])
def list_books():
    """Return list of all books."""
    return jsonify(books)

@app.route('/books/search', methods=['GET'])
def search_books():
    """Search books by author, year or genre."""
    author = request.args.get('author')
    published_year = request.args.get('published_year')
    genre = request.args.get('genre')
    
    filtered_books = books
    
    if author:
        filtered_books = [book for book in filtered_books 
                         if book['author'].lower() == author.lower()]
    if published_year:
        filtered_books = [book for book in filtered_books 
                         if str(book['published_year']) == published_year]
    if genre:
        filtered_books = [book for book in filtered_books 
                         if book.get('genre', '').lower() == genre.lower()]
    
    return jsonify(filtered_books)

@app.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    """Delete a book by ISBN."""
    for i, book in enumerate(books):
        if book['isbn'] == isbn:
            del books[i]
            return '', 204
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    """Update a book's details by ISBN."""
    data = request.json
    for book in books:
        if book['isbn'] == isbn:
            book.update(data)
            return jsonify(book), 200
    return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)