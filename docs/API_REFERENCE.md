# API Reference

## Base URL

All API endpoints are prefixed with `/api/v1`.

## Authentication

Currently, the API does not implement authentication mechanisms. This will be added in future versions.

## Error Handling

The API returns appropriate HTTP status codes and error messages in the following format:

```json
{
  "message": "Error message",
  "errors": {
    "field1": ["Error details for field1"],
    "field2": ["Error details for field2"]
  }
}
```

Common HTTP status codes:
- `200 OK`: Request succeeded
- `201 Created`: Resource created successfully
- `204 No Content`: Request succeeded, no content to return
- `400 Bad Request`: Invalid request parameters
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server-side error

## Resources

### Users

A user resource has the following structure:

```json
{
  "id": 1,
  "username": "johndoe",
  "email": "johndoe@example.com",
  "created_at": "2025-03-02T10:15:30.123456",
  "updated_at": "2025-03-02T10:15:30.123456"
}
```

#### GET /users

Returns a list of all users.

**Response**
- `200 OK`: Array of user objects

#### POST /users

Creates a new user.

**Request Body**
```json
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "password": "securepassword123"
}
```

**Validation Rules**
- `username`: Required, 3-64 characters
- `email`: Required, valid email format
- `password`: Required, minimum 6 characters

**Response**
- `201 Created`: The created user object (password excluded)
- `400 Bad Request`: Validation errors

#### GET /users/{id}

Returns a specific user by ID.

**Parameters**
- `id`: User ID (integer)

**Response**
- `200 OK`: User object
- `404 Not Found`: User not found

#### PUT /users/{id}

Updates a specific user.

**Parameters**
- `id`: User ID (integer)

**Request Body** (all fields optional)
```json
{
  "username": "newusername",
  "email": "newemail@example.com",
  "password": "newpassword123"
}
```

**Response**
- `200 OK`: Updated user object
- `400 Bad Request`: Validation errors
- `404 Not Found`: User not found

#### DELETE /users/{id}

Deletes a specific user.

**Parameters**
- `id`: User ID (integer)

**Response**
- `204 No Content`: User deleted successfully
- `404 Not Found`: User not found

## Examples

### Create a user

```bash
curl -X POST http://localhost:8080/api/v1/users \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "johndoe@example.com",
    "password": "securepassword123"
  }'
```

### Get all users

```bash
curl http://localhost:8080/api/v1/users
```

### Get a specific user

```bash
curl http://localhost:8080/api/v1/users/1
```

### Update a user

```bash
curl -X PUT http://localhost:8080/api/v1/users/1 \
  -H "Content-Type: application/json" \
  -d '{
    "email": "newemail@example.com"
  }'
```

### Delete a user

```bash
curl -X DELETE http://localhost:8080/api/v1/users/1
```