from pydantic import BaseModel
from typing import  Any

class TextResponse(BaseModel):
    user_id : str
    messages_to_bot : str
    messages_response : Any