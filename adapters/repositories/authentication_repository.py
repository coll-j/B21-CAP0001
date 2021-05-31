from entities.blacklisted_tokens import BlacklistToken
from flask.json import jsonify
from entities.user import User

class AuthenticationRepository:
  @staticmethod
  def login(username) -> dict:
    result: dict = {}
    user = User.query.filter_by(username=username).first()
    if not user:
      result = {
        'status': 'fail',
        'code': 401,
        'message': 'User not found.',
        'auth_token': None,
        'data': {},
      }
    else:
      auth_token = user.encode_auth_token(user.id)
      if auth_token:
        result = {
            'status': 'success',
            'code': 200,
            'message': 'Successfully logged in.',
            'auth_token': auth_token.decode(),
            'data': {
              'email': user.email,
              'username': user.username
            },
        }
        
      else:
        result = {
          'status': 'fail',
          'code': 500,
          'message': 'Some error occurred. Please try again.',
          'auth_token': None,
          'data': {},
        }
    
    return result

  @staticmethod
  def register(email, username, password) -> dict:
    user = User.query.filter_by(email=email).first()
    if not user:
      try:
        newUser = User(email, username, password)
        newUser.save()
        result = {
          'status': 'success',
          'code': 201,
          'message': 'Successfully registered.',
          'auth_token': None,
          'data': {},
        }

        return result
      except Exception as e:
        result = {
          'status': 'fail',
          'code': 401,
          'message': 'Some error occurred. Please try again. ({})'.format(e),
          'auth_token': None,
          'data': {},
        }
        return result
    else:
      User.rollback()
      result = {
        'status': 'fail',
        'code': 202,
        'message': 'User already exists. Please Log in.',
        'auth_token': None,
        'data': None,
      }
      return result

  @staticmethod
  def logout(auth_header):
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''
    if auth_token:
        resp = User.decode_auth_token(auth_token)
        if not isinstance(resp, str):
            # mark the token as blacklisted
            blacklist_token = BlacklistToken(auth_token)
            try:
                blacklist_token.save()
                result = {
                    'status': 'success',
                    'code': 200,
                    'message': 'Successfully logged out.',
                    'auth_token': None,
                    'data': {}
                }
                return result
            except Exception as e:
                result = {
                    'status': 'fail',
                    'code': 200,
                    'message': str(e),
                    'auth_token': None,
                    'data': {}
                }
                return result
        else:
            print("sini")
            result = {
                'status': 'fail',
                'code': 401,
                'message': resp,
                'auth_token': None,
                'data': {}
            }
            return result
    else:
        result = {
            'status': 'fail',
            'status': 403,
            'message': 'Provide a valid auth token.',
            'auth_token': None,
            'data': {}
        }
        return result