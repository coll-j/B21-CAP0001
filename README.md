# B21-CAP0001 (Cloud)
Hoax & hate speech game [backend]

## AUTHENTIFICATION

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