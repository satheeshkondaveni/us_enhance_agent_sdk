from app.business.story_enhancer import StoryEnhancer

if __name__ == "__main__":
    input_json = {
        "message": "success",
        "status": True,
        "user_feedback": "Add clarity to acceptance criteria",
        "user_stories": [{
            "title": "Login functionality",
            "description": "As a user, I want to log in",
            "acceptance_criteria": ""
        }]
    }

    agent = StoryEnhancer(
        username="dev_user",
        password="secure_pass",
        genai_model="ollama",
        embedding_model="bge"   # Using BGE embedding model
    )

    result = agent.enhance_userstories(input_json)
    print(result)
