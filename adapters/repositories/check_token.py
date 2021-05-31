from entities.blacklisted_tokens import BlacklistToken
from entities.user import User

def check_token(auth_header):
  if auth_header:
      auth_token = auth_header.split(" ")[1]
  else:
      auth_token = ''

  if not auth_token:
    result = {
        'status': 'fail',
        'code': 401,
        'message': "Auth token not valid",
        'auth_token': None,
        'data': {}
    }
    return result
  
  resp = User.decode_auth_token(auth_token)
  if not isinstance(resp, str):
      result = {
        'status': 'success',
        'code': 200,
        'message': 'User authorized',
        'auth_token': None,
        'data': {},
      }

      return result
  else:
    result = {
        'status': 'fail',
        'code': 401,
        'message': str(resp),
        'auth_token': None,
        'data': {}
    }
    return result