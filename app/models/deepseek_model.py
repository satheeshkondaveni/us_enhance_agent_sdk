
from app.models.base_models.base_model import BaseModel
import requests

class DeepseekModel(BaseModel):
    """
    Deepseek GenAI model integration.
    """

    def connect(self):
        self.host = self.config.get("DEEPSEEK_HOST")
        self.model = self.config.get("DEEPSEEK_MODEL")
        self.api_key = self.config.get("DEEPSEEK_API_KEY")
        if not self.host or not self.model or not self.api_key:
            raise Exception("Deepseek configuration missing")

    def generate(self, prompt: str) -> str:
        try:
            headers = {"Authorization": f"Bearer {self.api_key}"}
            response = requests.post(
                f"{self.host}/v1/generate",
                headers=headers,
                json={"model": self.model, "prompt": prompt}
            )
            if response.status_code == 200:
                return response.json().get("output", "")


        except Exception as e:
            print(f"Deepseek API error: ", e)


