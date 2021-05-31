from entities.blacklisted_tokens import BlacklistToken
from flask.json import jsonify
from entities.user import User

class LevelRepository:
  @staticmethod
  def levels(auth_header):
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''
    if auth_token:
        resp = User.decode_auth_token(auth_token)
        if not isinstance(resp, str):
            # mark the token as blacklisted
            blacklist_token = BlacklistToken(token=auth_token)
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
                    'message': e,
                    'auth_token': None,
                    'data': {}
                }
                return result
        else:
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
