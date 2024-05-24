from fastapi import APIRouter
from models.responseModel import APIResponse
from textResponse.models.textModel import TextResponse
from textResponse.infrastructure.textResponseInfra import *

router = APIRouter()

@router.post("/", response_model=APIResponse)
def get_text_response(message:TextResponse):
    return getGPTResponse(message)

@router.post("/voice", response_model=APIResponse)
def get_voice_response(user, message):
    return getGPTVoiceResponse(user, message)

@router.post("/image", response_model=APIResponse)
def get_image_response(user, image):
    return getGPTImageResponse(user, image)