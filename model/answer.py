from pydantic import BaseModel,ConfigDict
from typing import Any

class Answer(BaseModel): 
    model_config = ConfigDict(arbitrary_types_allowed=True)
    type: str in ['text', 'radio', 'checkbox', 'picklist', 'number', 'date', 'datetime', 'email', 'phone']
    value: Any
    hasError: bool = False