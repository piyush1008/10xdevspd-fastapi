# FastAPI User & Post Service

This is a simple FastAPI application for managing users and posts using MongoDB.

## Prerequisites

- Python 3.7+
- MongoDB instance (Atlas or local)

## Installation

1.  **Clone the repository:**
    ```bash
    # If the user is cloning for the first time
    git clone <repository_url>
    cd fastApi
    ```

2.  **Set up a virtual environment:**

    It is recommended to use a virtual environment to manage dependencies for your project.

    -   **Windows:**
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    -   **macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install dependencies:**
    After activating the virtual environment, install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the application, use `uvicorn`. This command will start the server with hot-reload enabled, which is useful for development.

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

-   **Health Check**: `GET /`
-   **Users**:
    -   Create User: `POST /users`
    -   Get All Users: `GET /users`
    -   Get User by ID: `GET /users/{id}`
    -   Delete User: `DELETE /users/{id}`
-   **Posts**:
    -   Create Post: `POST /posts`
    -   Get Post by ID: `GET /post/{id}`
