from exception.error import UnexpectedError, ValidationError
from flask import Blueprint

from adapters.controllers.handler import handle_validation_error, handle_unexpected_error

errors = Blueprint("errors", __name__)

@errors.app_errorhandler(ValidationError)
def validation_error(error):
  return handle_validation_error(error)

@errors.app_errorhandler(UnexpectedError)
def unexpected_error(error):
    return handle_unexpected_error(error)