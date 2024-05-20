from fastapi import APIRouter
from models.responseModel import APIResponse
from textResponse.infrastructure.textResponseInfra import *

router = APIRouter()

@router.post("/", response_model=APIResponse)
def get_text_response(user, prompt,gender):
    return getGPTResponse(user, prompt,gender)

@router.post("/voice", response_model=APIResponse)
def get_voice_response(user, message):
    return getGPTVoiceResponse(user, message)

@router.post("/image", response_model=APIResponse)
def get_image_response(user, image):
    return getGPTImageResponse(user, image)