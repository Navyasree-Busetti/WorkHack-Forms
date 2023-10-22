from pydantic import BaseModel, Field, ConfigDict
from model.question import Question
from typing import Union, Optional
import model.constants as constants

class Form(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    id: int = Field(default = None)
    name: str
    description: Union[str, None]
    questions: list[Question]
    status: str in ['draft', 'published'] = 'draft'
    actions: Optional[list[str]] = None

    def __init__(self, **data):
        super().__init__(**data)
        if self.id == None:
            constants.ids['Form'] = constants.ids.get('Form') + 1
            self.id = constants.ids.get('Form')
        else:
            for question in self.questions:
                if question.id != None and question.delete == True:
                    self.questions.remove(question)
                    