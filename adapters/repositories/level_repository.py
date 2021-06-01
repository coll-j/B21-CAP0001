from flask.json import jsonify
from entities.user_levels import UserLevels
from entities.level import Level
from entities.mapping_level import MappingLevel
from adapters.helpers.token import Token
from adapters.helpers.session import session
from flask import jsonify

class LevelRepository:
    @staticmethod
    def levels(auth_header):
        user_id, auth_token, result = Token.get_token_and_user(auth_header=auth_header)
        if user_id:
            levels = []
            levels_temp = []
            levels_done = session.query(
                UserLevels
            ).filter(
                UserLevels.user_id == user_id
            ).all()

            if len(levels_done) < 1:
                level = Level.query.filter_by(level=1).first()
                levels_temp.append(level)
            else:
                levels_id = set()
                for level in levels_done:
                    mapping_level = MappingLevel.query.filter_by(level_before=level.id).first()
                    levels_id.add(mapping_level.level_before)
                    levels_id.add(mapping_level.level_next)

                for level_id in levels_id:
                    level = Level.query.filter_by(id=level_id).first()
                    levels_temp.append(level)

            for level in levels_temp:
                levels.append(level.as_dict())

            result["message"] = 'success'
            result["data"] = {
                'levels': levels
            }

            return result
        else:
            return result
