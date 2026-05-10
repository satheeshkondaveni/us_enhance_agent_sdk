import os
from dotenv import dotenv_values

class EnvLoader:
    """
    Utility class to load environment variables from .env files.
    Used for model connection properties (Ollama, Deepseek, BGE, etc.).
    """

    @staticmethod
    def load_env(file_path: str) -> dict:
        """
        Load environment variables from a given .env file.

        Args:
            file_path (str): Path to the .env file.

        Returns:
            dict: Dictionary of environment variables.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Config file not found: {file_path}")

        config = dotenv_values(file_path)
        if not config:
            raise ValueError(f"Failed to load environment variables from {file_path}")

        return config

    @staticmethod
    def get_env_var(file_path: str, key: str) -> str:
        """
        Retrieve a specific environment variable from a .env file.

        Args:
            file_path (str): Path to the .env file.
            key (str): Environment variable key.

        Returns:
            str: Value of the environment variable.
        """
        config = EnvLoader.load_env(file_path)
        value = config.get(key)
        if value is None:
            raise KeyError(f"Key '{key}' not found in {file_path}")
        return value
