from GPT.gptModel import GPT
from fastapi import HTTPException
from models.responseModel import APIResponse
from textResponse.models.textModel import TextResponse

def getGPTResponse(user,prompt) -> APIResponse:
    try:
        return APIResponse(
            message="Success",
            data=TextResponse(
                user_id=user,
                messages_to_bot=prompt,
                messages_response=GPT().chat_message(prompt)
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