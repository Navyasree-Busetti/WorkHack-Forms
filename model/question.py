from pydantic import BaseModel, Field
from model.answer import Answer
import model.constants as constants

class Question(BaseModel):
    id: int = Field(default = None)
    label: str
    answer : Answer
    delete: bool = Field(default=False)

    def __init__(self, **data):
        super().__init__(**data)
        if self.id == None:
            constants.ids['Question'] = constants.ids.get('Question') + 1
            self.id = constants.ids.get('Question')