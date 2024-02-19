# pyTODO

A TODO API

## Features

- User authentication
- Create, read, update, and delete todos
- User-specific todos

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (for running the server)
- Pydantic

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/malbertzard/pyTODO.git
   cd pyTODO
   ```


## Usage

1. Run the FastAPI application using Uvicorn:

   ```bash
   make run
   ```

2. Change .env.local for other runtimes etc
   ```bash
   cp .env .env.local
   ```

3. Open your web browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore the API documentation and test the endpoints using Swagger UI.

## API Endpoints

- **POST /todos/**: Create a new todo.
- **GET /todos/**: Retrieve a list of todos.
- **GET /todos/{uid}**: Retrieve a specific todo by UID.
- **PUT /todos/{uid}**: Update a specific todo by UID.
- **DELETE /todos/{uid}**: Delete a specific todo by UID.

For more detailed information, refer to the [API documentation](http://127.0.0.1:8000/docs) while the server is running.
