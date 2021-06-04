## AUTHENTICATION METHOD

### [POST] LOGIN
Request:
- Method: POST
- Endpoint: `/auth/login`
- Header:
    - Content-Type: application/json
    - Accept: application/json
- Body:
```json
{
    "id": "integer",
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

### [POST] REGISTER
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

### [POST] LOGOUT
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

<br/>

## IN GAME METHOD

### [GET] LIST LEVEL 
#### Showing opened (available) Level for a User

<br/>

Request:
- Method: GET
- Endpoint: `/level/`
- Header:
    - Content-Type: application/json
    - Accept: application/json
    - Authorization: Bearer Token

Response:
```json
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

<hr/>

### [GET] LEVEL DETAIL
#### Get gameplay from selected level

<br/>

Request:
- Method: GET
- Endpoint: `/level/{level_id}`
- Header:
    - Content-Type: application/json
    - Accept: application/json
    - Authorization: Bearer Token

Response:
```json
{
    "auth_token": "string",
    "code": "integer",
    "data": {
        "answer_choices": [
            {
                "id": "integer",
                "mapping_level_id": "integer",
                "question_id": "integer",
                "text": "string"
            },
        ],
        "facts": [
            {
                "id": "integer",
                "question_id": "integer",
                "text": "string"
            },
        ],
        "question": {
            "id": "integer",
            "is_multiple_choices": "boolean",
            "level_id": "integer",
            "text": "string"
        }
    },
    "message": "string",
    "status": "string"
}
```

<hr/>

### [GET] Badge
#### Showing badge that user have been achieved

<br/>

Request:
- Method: GET
- Endpoint: `/badge/`
- Header:
    - Content-Type: application/json
    - Accept: application/json
    - Authorization: Bearer Token

Response:
```json
{
    "auth_token": "string",
    "code": "integer",
    "data": {
        "badges": [
            {
                "description": "string",
                "gambar": "string",
                "id": "integer",
                "title": "string"
            }
        ]
    },
    "message": "string",
    "status": "string"
}
```

<hr/>