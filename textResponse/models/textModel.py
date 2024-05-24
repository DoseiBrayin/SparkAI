from pydantic import BaseModel
from typing import  Any, Optional

class TextResponse(BaseModel):
    user_id : str
    chat_id: str
    gender : int
    message_user : Any
    messages_response : Any
    timestamp : Any
    metadata : Optional[dict] = None
