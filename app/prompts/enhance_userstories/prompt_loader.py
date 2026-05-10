import os

class PromptLoader:
    @staticmethod
    def load_prompts():
        base_path = "app/prompts/enhance_userstories"
        return {
            "system": open(os.path.join(base_path, "system.txt")).read(),
            "user": open(os.path.join(base_path, "user.txt")).read(),
            "output": open(os.path.join(base_path, "output_format.txt")).read()
        }
