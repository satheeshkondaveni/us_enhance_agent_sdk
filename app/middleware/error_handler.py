from app.loggins.logger import get_logger
from app.exceptions.auth_exceptions import AuthenticationError
from app.exceptions.model_exceptions import ModelConnectionError
from app.exceptions.validation_exceptions import ValidationError

log = get_logger()

class ErrorHandlerMiddleware:
    @staticmethod
    def handle_error(error: Exception):
        if isinstance(error, AuthenticationError):
            log.error(f"Authentication failed: {error}")
        elif isinstance(error, ModelConnectionError):
            log.error(f"Model connection error: {error}")
        elif isinstance(error, ValidationError):
            log.error(f"Validation error: {error}")
        else:
            log.error(f"Unexpected error: {error}")
        return {"message": "error", "status": False, "details": str(error)}
