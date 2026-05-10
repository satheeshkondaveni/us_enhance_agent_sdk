class AuthenticationError(Exception):
    """Raised when authentication fails."""
    def __init__(self, message="Invalid username or password"):
        super().__init__(message)
