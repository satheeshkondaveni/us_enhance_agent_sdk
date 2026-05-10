from pydantic import BaseModel, ValidationError
from typing import List

class UserStory(BaseModel):
    title: str
    description: str
    acceptance_criteria: str

class InputValidator:
    @staticmethod
    def validate(input_json):
        try:
            for story in input_json["user_stories"]:
                UserStory(**story)
        except ValidationError as e:
            raise Exception(f"Validation failed: {e}")
