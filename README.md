# Flask REST API Project

A professional Flask REST API with a modular structure, SQLAlchemy integration, and proper separation of concerns.

## Project Structure

```
prueba-api/
├── app/                    # Application package
│   ├── api/                # API endpoints
│   │   └── v1/             # API version 1
│   │       ├── resources/  # API resources
│   │       └── ...
│   ├── models/             # Database models
│   ├── schemas/            # Marshmallow schemas for serialization
│   ├── services/           # Business logic
│   ├── config/             # Configuration
│   ├── utils/              # Utility modules
│   └── tests/              # Tests
│       ├── unit/           # Unit tests
│       └── integration/    # Integration tests
├── migrations/             # Database migrations
├── docs/                   # Documentation
├── scripts/                # Utility scripts
├── requirements.txt        # Dependencies
├── .env.example            # Environment variables example
└── run.py                  # Application entry point
```

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file based on `.env.example`
5. Initialize the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

## Running the Application

First, activate the virtual environment:

```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Then start the Flask application:

```bash
# Option 1: Using the run.py script
python run.py

# Option 2: Using Flask CLI
flask run --port 8080
```

## API Endpoints

For detailed API documentation, see [API Reference](docs/API_REFERENCE.md).

### Health Check

- **URL:** `/api/v1/health`
- **Method:** `GET`
- **Description:** Check if the API is running
- **Success Response:**
  - **Code:** 200
  - **Content:** `{ "status": "OK" }`

### User Endpoints

#### Get All Users

- **URL:** `/api/v1/users`
- **Method:** `GET`
- **Description:** Retrieve a list of all users
- **Success Response:**
  - **Code:** 200
  - **Content:** Array of user objects
    ```json
    [
      {
        "id": 1,
        "username": "admin",
        "email": "admin@example.com",
        "created_at": "2025-03-02T09:12:21.955249",
        "updated_at": "2025-03-02T09:12:21.955258"
      },
      ...
    ]
    ```

#### Create User

- **URL:** `/api/v1/users`
- **Method:** `POST`
- **Description:** Create a new user
- **Request Body:**
  ```json
  {
    "username": "johndoe",
    "email": "johndoe@example.com",
    "password": "securepassword123"
  }
  ```
- **Required Fields:**
  - `username`: String, 3-64 characters
  - `email`: Valid email format
  - `password`: String, minimum 6 characters
- **Success Response:**
  - **Code:** 201 CREATED
  - **Content:** The created user object (password excluded)
    ```json
    {
      "id": 3,
      "username": "johndoe",
      "email": "johndoe@example.com",
      "created_at": "2025-03-02T10:15:30.123456",
      "updated_at": "2025-03-02T10:15:30.123456"
    }
    ```
- **Error Response:**
  - **Code:** 400 BAD REQUEST
  - **Content:** Error messages
    ```json
    {
      "message": "Validation error",
      "errors": {
        "username": ["Length must be between 3 and 64."],
        "email": ["Not a valid email address."],
        "password": ["Length must be at least 6."]
      }
    }
    ```

#### Get User by ID

- **URL:** `/api/v1/users/{id}`
- **Method:** `GET`
- **URL Params:** 
  - `id`: User ID (integer)
- **Description:** Retrieve a specific user by ID
- **Success Response:**
  - **Code:** 200
  - **Content:** User object
    ```json
    {
      "id": 1,
      "username": "admin",
      "email": "admin@example.com",
      "created_at": "2025-03-02T09:12:21.955249",
      "updated_at": "2025-03-02T09:12:21.955258"
    }
    ```
- **Error Response:**
  - **Code:** 404 NOT FOUND
  - **Content:** `{ "message": "User not found" }`

#### Update User

- **URL:** `/api/v1/users/{id}`
- **Method:** `PUT`
- **URL Params:** 
  - `id`: User ID (integer)
- **Description:** Update a specific user
- **Request Body:** Any combination of these fields
  ```json
  {
    "username": "newusername",
    "email": "newemail@example.com",
    "password": "newpassword123"
  }
  ```
- **Success Response:**
  - **Code:** 200
  - **Content:** Updated user object
    ```json
    {
      "id": 1,
      "username": "newusername",
      "email": "newemail@example.com",
      "created_at": "2025-03-02T09:12:21.955249",
      "updated_at": "2025-03-02T10:45:12.345678"
    }
    ```
- **Error Responses:**
  - **Code:** 404 NOT FOUND
    - **Content:** `{ "message": "User not found" }`
  - **Code:** 400 BAD REQUEST
    - **Content:** Validation error messages

#### Delete User

- **URL:** `/api/v1/users/{id}`
- **Method:** `DELETE`
- **URL Params:** 
  - `id`: User ID (integer)
- **Description:** Delete a specific user
- **Success Response:**
  - **Code:** 204 NO CONTENT
- **Error Response:**
  - **Code:** 404 NOT FOUND
  - **Content:** `{ "message": "User not found" }`

## Testing

```bash
pytest
```

## Adding New Resources

To add a new resource:

1. Create a model in `app/models/`
2. Create a schema in `app/schemas/`
3. Create a service in `app/services/`
4. Create a resource in `app/api/v1/resources/`
5. Register the resource in `app/api/v1/routes.py`