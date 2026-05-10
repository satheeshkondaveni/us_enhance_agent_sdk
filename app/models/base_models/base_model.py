from app.utils.env_loader import EnvLoader

class BaseModel:
    def __init__(self, config_file):
        self.config = EnvLoader.load_env(config_file)

    def connect(self):
        raise NotImplementedError("Subclasses must implement connect()")
