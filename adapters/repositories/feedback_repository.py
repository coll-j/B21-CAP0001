from adapters.repositories.check_token import check_token
from entities.level import Level
from entities.blacklisted_tokens import BlacklistToken
from entities.user import User
from entities.feedback import Feedback

class FeedbackRepository:
  @staticmethod
  def get_feedback(level_id, auth_header) -> dict:

    check_result = check_token(auth_header)

    if check_result['code'] == 200:
      feedback = Feedback.query.filter_by(level_id=level_id).first()
      if not feedback:
        check_result["message"] = 'Feedback not found'
        return check_result
      else:
        level = Level.query.filter_by(id=level_id).first()

        check_result["message"] = 'Feedback found'
        check_result["data"] = {
          'feedback': feedback,
          'level': level
        }
        return check_result
    else:
      return check_result