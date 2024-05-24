from typing import List, Optional
from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, *args, **kwargs):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, *args, **kwargs):
        return {
            "title": "ObjectId",
            "type": "string",
            "pattern": "^[a-fA-F0-9]{24}$",
            "examples": ["5f7d1b1d8fd2b84222fae91c"]
        }
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

    def __str__(self):
        return str(self.binary)

class MessagesModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    sender: str
    type: str
    messages: str
    metadata: Optional[dict] = None  
    timestamp: datetime
    
    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            PyObjectId: str
        }

    def to_dict(self):
        return {
            "_id": str(self.id),
            "sender": self.sender,
            "type": self.type,
            "messages": self.messages,
            "metadata": self.metadata,
            "timestamp": self.timestamp
        }

class ChatModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    user_id: str
    chat_with: str
    messages: List[MessagesModel] = []

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            PyObjectId: str
        }
    
    def to_dict(self):
        return {
            "_id": str(self.id),
            "user_id": self.user_id,
            "chat_with": self.chat_with,
            "messages": [message.to_dict() for message in self.messages]
        }