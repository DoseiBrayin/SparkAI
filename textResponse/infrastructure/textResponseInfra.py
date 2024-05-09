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
                messages_response=GPT().complete(prompt)
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