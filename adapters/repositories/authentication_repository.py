from entities.user import User

class AuthenticationRepository:
  @staticmethod
  def login(username) -> dict:
    user: dict = {}
    user = User.query.filter_by(username=username).first_or_404()
    user = {
      'uuid': user.uuid,
      'name': user.name,
      'username': user.username,
    }
    return user
