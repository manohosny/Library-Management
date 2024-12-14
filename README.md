# Library Management System API

A RESTful API for managing a library's book collection, built with Flask and containerized with Docker.

## Getting Started

### Prerequisites
- Docker installed on your system
- Git (optional, for cloning the repository)

### Building and Running with Docker

1. Build the Docker image:
```bash
docker build -t library-api .
```

2. Run the container:
```bash
docker run -d -p 4000:4000 library-api
```

The API will be available at `http://localhost:4000`

### API Documentation

The API documentation is available through Swagger UI:

1. Open your web browser and navigate to:
```
http://localhost:4000/api-docs
```

2. From the Swagger UI, you can:
   - View all available endpoints
   - Test API endpoints directly
   - View request/response schemas
   - Execute sample requests

### Available Endpoints

- `POST /books` - Add a new book
- `GET /books` - List all books
- `GET /books/search` - Search books by author, year, or genre
- `DELETE /books/{isbn}` - Delete a book by ISBN
- `PUT /books/{isbn}` - Update book details

### Example API Usage

Add a new book:
```bash
curl -X POST http://localhost:4000/books \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Sample Book",
    "author": "John Doe",
    "published_year": 2023,
    "isbn": "978-0-123456-47-2",
    "genre": "Fiction"
  }'
```

### Stopping the Container

To stop the running container:
1. Find the container ID:
```bash
docker ps
```

2. Stop the container:
```bash
docker stop <container_id>
```