from app.business.story_enhancer import StoryEnhancer

class UserStoryEnhanceAgent:
    def __init__(self, username, password, genai_model="ollama", embedding_model="bge"):
        self.enhancer = StoryEnhancer(
            username=username,
            password=password,
            genai_model=genai_model,
            embedding_model=embedding_model
        )

    def run(self, input_json):
        """
        Entry point for the agent.
        Enhances user stories using the selected GenAI + embedding model.
        """
        return self.enhancer.enhance_userstories(input_json)
