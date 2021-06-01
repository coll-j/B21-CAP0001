from adapters.repositories.check_token import check_token
from entities.user import User

class Token:
    @staticmethod
    def get_token_and_user(auth_header):
        user = None
        token = None
        result = None

        if auth_header:
            result = check_token(auth_header)

            if result['code'] == 200:
                token = auth_header.split(" ")[1]
                if token:
                    user = User.decode_auth_token(token)

        return user, token, result
