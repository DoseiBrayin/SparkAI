from bson import ObjectId
from pydantic import Field
from db.mongoConection import chats_collection
from textResponse.models.chatModel import ChatModel
from models.responseModel import APIResponse


# Get all chat rooms
# Obtener todas las salas de chat
def get_all_chat_rooms():
    chats = chats_collection.find()
    return APIResponse(data=[{**chat, "_id": str(chat["_id"])} for chat in chats], message="Chats retrieved successfully", status="success",status_code=200)

def create_chat_room(chat: ChatModel):
    chat_dict = chat.dict(by_alias=True)
    chat_dict["_id"] = ObjectId()  # Genera un nuevo ObjectId
    result = chats_collection.insert_one(chat_dict)
    return result.inserted_id

def get_chats_by_user_id(user_id):
    chats = chats_collection.find({"user_id": user_id})
    return APIResponse(data=[{**chat, "_id": str(chat["_id"])} for chat in chats], message="Chats retrieved successfully", status="success",status_code=200)