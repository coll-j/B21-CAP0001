from entities.user import User

class Token:
    @staticmethod
    def get_token_and_user(auth_header):
        user = None
        token = None

        if auth_header:
            token = auth_header.split(" ")[1]
            if token:
                user = User.decode_auth_token(token)

        return user, token
