class ValidationError(Exception):
    """Raised when input validation fails."""
    def __init__(self, message="Input validation error"):
        super().__init__(message)
