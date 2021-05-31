from entities.user_levels import UserLevels
from adapters.repositories.check_token import check_token


class InGameRepository:
  @staticmethod
  def save_game(user_id, level_id, auth_header) -> dict:
    result = check_token(auth_header)

    if result['code'] == 200:
      level = UserLevels.query.filter_by(user_id=user_id, level_id=level_id).first()
      
      if not level:
        try:
          levels = UserLevels(user_id, level_id)
          levels.save()

          result["message"] = 'Successfully saved.'
          result["code"] = 201

          return result
        except Exception as e:

          result["message"] = 'Some error occurred. Please try again. ({})'.format(e)
          result["code"] = 500

          return result
      else:
        result["message"] = 'Saved game exist, load it.'
        return result
    else:
      return result

  @staticmethod
  def get_saved_game(user_id, auth_header) -> dict:
    result = check_token(auth_header)

    if result['code'] == 200:
      levels = []
      levels = UserLevels.query.filter_by(user_id=user_id)
    
      result["message"] = 'success.'
      result["data"] = {
        'user_levels': levels
      }

      return result
    else:
      return result