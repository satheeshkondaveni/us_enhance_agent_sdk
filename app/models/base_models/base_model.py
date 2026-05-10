from app.utils.env_loader import load_env

class BaseModel:
    def __init__(self, config_file):
        self.config = load_env(config_file)

    def connect(self):
        raise NotImplementedError("Subclasses must implement connect()")
