class InGameRepository:
  @staticmethod
  def save_game(user_id, level_id) -> dict:
    result: dict = {}