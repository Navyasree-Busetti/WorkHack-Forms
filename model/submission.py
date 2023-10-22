from pydantic import BaseModel, Field
from model.question import Question
import model.constants as constants

class Submission(BaseModel):
    id: int = Field(default = None) #form id
    questions: list[Question]
