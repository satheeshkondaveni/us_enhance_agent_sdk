class ModelConnectionError(Exception):
    """Raised when a GenAI or embedding model fails to connect."""
    def __init__(self, model_name, message="Model connection failed"):
        super().__init__(f"{model_name}: {message}")

