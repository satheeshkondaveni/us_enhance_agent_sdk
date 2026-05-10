from app.auth.authenticator import Authenticator
from app.models.ollama_model import OllamaModel
from app.models.deepseek_model import DeepseekModel
from app.models.embedding.bge_model import BGEModel
from app.prompts.enhance_userstories.prompt_loader import PromptLoader
from app.validators.userstory_validator import InputValidator

class StoryEnhancer:
    def __init__(self, username, password, genai_model, embedding_model):
        self.auth = Authenticator(username, password, genai_model, embedding_model)
        self.genai_model = genai_model
        self.embedding_model = embedding_model

    def enhance_userstories(self, input_json):
        # Step 1: Validate user
        self.auth.validate_user()

        # Step 2: Validate input JSON
        InputValidator.validate(input_json)

        # Step 3: Connect to GenAI model
        if self.genai_model == "ollama":
            model = OllamaModel("config/models/gen_ai/ollama.env")
        elif self.genai_model == "deepseek":
            model = DeepseekModel("config/models/gen_ai/deepseek.env")
        else:
            raise Exception("Unsupported GenAI model")
        model.connect()

        # Step 4: Connect to embedding model
        if self.embedding_model == "bge":
            embed_model = BGEModel("config/models/embedding/bge.env")
        else:
            raise Exception("Unsupported embedding model")
        embed_model.connect()

        # Step 5: Load prompts
        prompts = PromptLoader.load_prompts()

        # Step 6: Use Ollama/Deepseek to enhance stories
        enhanced_stories = []
        for story in input_json["user_stories"]:
            prompt = f"""
            {prompts['system']}
            User Feedback: {input_json.get('user_feedback', '')}
            Title: {story['title']}
            Description: {story['description']}
            Acceptance Criteria: {story['acceptance_criteria']}
            {prompts['output']}
            """
            enhanced_output = model.generate(prompt)
            # embed_vector = embed_model.embed(enhanced_output)  # semantic validation
            enhanced_stories.append(enhanced_output)

        return {
            "message": "success",
            "status": True,
            "user_feedback": input_json.get("user_feedback", ""),
            "user_stories": enhanced_stories
        }
