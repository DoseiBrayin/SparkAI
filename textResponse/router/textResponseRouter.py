from fastapi import APIRouter
from models.responseModel import APIResponse
from textResponse.infrastructure.textResponseInfra import getGPTResponse, getGPTVoiceResponse

router = APIRouter()

@router.post("/", response_model=APIResponse)
def get_text_response(user, prompt):
    return getGPTResponse(user, prompt)

@router.post("/voice", response_model=APIResponse)
def get_voice_response(user, message):
    return getGPTVoiceResponse(user, message)