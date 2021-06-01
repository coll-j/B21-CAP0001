# B21-CAP0001 (Cloud)
Hoax & hate speech game [backend]

## AUTHENTICATION

### LOGIN
Request:
- Method: POST
- Endpoint: `/auth/login`
- Header:
    - Content-Type: application/json
    - Accept: application/json
- Body:
```json
{
    "email": "string",
    "password": "string"
}
```

Response:
```json
{
  "auth_token": "string",
  "code": "integer",
  "data": {
    "email": "string",
    "username": "string"
  },
  "message": "string",
  "status": "string"
}
```

### REGISTER
Request:
- Method: POST
- Endpoint: `/auth/register`
- Header:
    - Content-Type: application/json
    - Accept: application/json
- Body:
```json
{
    "email": "string",
    "username": "string",
    "password": "string"
}
```

Response:
```json
{
  "auth_token": "string",
  "code": "integer",
  "data": {},
  "message": "string",
  "status": "string"
}
```

### LOGOUT [FIXING]
Request:
- Method: POST
- Endpoint: `/auth/logout`
- Header:
    - Content-Type: application/json
    - Accept: application/json
    - Authorization: Bearer Token

Response:
```json
{
  "auth_token": "string",
  "code": "integer",
  "data": {},
  "message": "string",
  "status": "string"
}
```

## Pengguna dapat mengakses level-level yang telah dan sedang dibuka untuk user tersebut

### Showing Opened Level for a User

Request:
- Method: GET
- Endpoint: `/level/`
- Header:
    - Content-Type: application/json
    - Accept: application/json
    - Authorization: Bearer Token

Response:
```json
// success
{
    "auth_token": "string",
    "code": "integer",
    "data": {
        "levels": [
            {
                "branch": "integer",
                "id": "integer",
                "level": "integer",
                "public_link": "string"
            }
        ]
    },
    "message": "string",
    "status": "string"
}
```
