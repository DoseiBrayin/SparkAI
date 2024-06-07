from GPT.gptModel import GPT
from fastapi import HTTPException
from bson import ObjectId
from models.responseModel import APIResponse
from textResponse.models.chatModel import MessagesModel
from textResponse.models.textModel import TextResponse
from datetime import datetime
from db.mongoConection import chats_collection
from models.trainModel import TrainModel
from helpers.promptModel import Prompt

def getTrainGPTResponse(message:TrainModel) -> APIResponse:

    p = Prompt(message.prompt, message.gender, message.personality)

    message_user = MessagesModel(
        id=ObjectId(),
        sender=message.user_id,
        type='text',
        messages=message.message_user,
        timestamp= message.timestamp if message.timestamp != None else datetime.now(),
        metadata= message.metadata if message.metadata != None else {}
    )

    chats_collection.update_one(
        {"user_id": message.user_id},
        {"$push": {"messages": message_user.to_dict()}}
    )

    message_bot = MessagesModel(
        id=ObjectId(),
        sender="bot",
        type='text',
        messages=GPT().train(p.to_dict(),user_id=message.user_id),
        timestamp= message.timestamp if message.timestamp != None else datetime.now(),
        metadata= message.metadata if message.metadata != None else {}
    )


    chats_collection.update_one(
        {"user_id": message.user_id},
        {"$push": {"messages": message_bot.to_dict()}}
    )

    return APIResponse(
        message="Success",
        data=message_bot.messages,
        status="SUCCESS",
        status_code=200
    )



def getGPTResponse(message:TextResponse) -> APIResponse:
    try:
        message_user = MessagesModel(
            id=ObjectId(),
            sender=message.user_id,
            type='text',
            messages=message.message_user,
            timestamp= message.timestamp if message.timestamp != None else datetime.now(),
            metadata= message.metadata if message.metadata != None else {}
        )

        message_bot = MessagesModel(
            id=ObjectId(),
            sender="bot",
            type='text',
            messages=GPT().chat_message(message.message_user,user_id=message.user_id),
            timestamp= message.timestamp if message.timestamp != None else datetime.now(),
            metadata= message.metadata if message.metadata != None else {}
        )

        chats_collection.update_one(
            {"user_id": message.user_id},
            {"$push": {"messages": message_user.to_dict()}}
        )

        chats_collection.update_one(
            {"user_id": message.user_id},
            {"$push": {"messages": message_bot.to_dict()}}
        )

        return APIResponse(
            message="Success",
            data=message_bot.messages,
            status="SUCCESS",
            status_code=200
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=APIResponse(
            message="Internal Server Error",
            data=str(e),
            status="ERROR",
            status_code=500
        ).__dict__)

def getGPTVoiceResponse(user:str,message:str) -> APIResponse:
    try:
        gpt_message = GPT().chat_message(message)
        return APIResponse(
            message="Success",
            data=TextResponse(
                user_id=user,
                messages_to_bot=gpt_message,
                messages_response=GPT(model='tts-1').voice_chat(gpt_message)
            ),
            status="SUCCESS",
            status_code=200
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=APIResponse(
            message="Internal Server Error",
            data=str(e),
            status="ERROR",
            status_code=500
        ).__dict__)

def getGPTImageResponse(user:str,image) -> APIResponse:
    try:
        return APIResponse(
            message="Success",
            data=TextResponse(
                user_id=user,
                messages_to_bot=image,
                messages_response=GPT().image_to_text(image)
            ),
            status="SUCCESS",
            status_code=200
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=APIResponse(
            message="Internal Server Error",
            data=str(e),
            status="ERROR",
            status_code=500
        ).__dict__)