from pydantic import BaseModel
from typing import  Any, Optional

class TrainModel(BaseModel):
    user_id : str
    chat_id: str
    gender : int
    message_user : Any
    prompt : str
    timestamp : Any
    metadata : Optional[dict] = None
    personality : str
