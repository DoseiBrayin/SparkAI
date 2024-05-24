from fastapi import APIRouter, Depends, HTTPException
from textResponse.models.chatModel import ChatModel
from textResponse.infrastructure.chatInfras import get_all_chat_rooms, create_chat_room

chats_router = APIRouter()

@chats_router.get("/chats")
async def get_chats():
    return get_all_chat_rooms()

@chats_router.post("/chat")
async def create_chat(chat_room: ChatModel):
    chat_room_id = create_chat_room(chat_room)
    return {"chat_room_id": str(chat_room_id)}