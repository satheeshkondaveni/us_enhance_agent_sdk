from app.models.base_models.base_model import BaseModel

class BGEModel(BaseModel):
    def connect(self):
        # Load BGE embedding model config
        endpoint = self.config.get("BGE_ENDPOINT")
        api_key = self.config.get("BGE_API_KEY")
        # Example: connect to HuggingFace or local inference
        return f"Connected to BGE model at {endpoint}"
