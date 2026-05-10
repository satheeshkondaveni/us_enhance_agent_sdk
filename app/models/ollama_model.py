from app.models.base_models.base_model import BaseModel
import requests

class OllamaModel(BaseModel):
    def connect(self):
        self.host = self.config.get("OLLAMA_HOST")
        self.model = self.config.get("OLLAMA_MODEL")

    def generate(self, prompt: str):
        response = requests.post(
            f"{self.host}/api/generate",
            json={"model": self.model, "prompt": prompt}
        )
        return response.json().get("output", "")
