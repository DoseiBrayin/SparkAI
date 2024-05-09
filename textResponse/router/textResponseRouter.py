from fastapi import APIRouter
from models.responseModel import APIResponse
from textResponse.infrastructure.textResponseInfra import getGPTResponse

router = APIRouter()

@router.post("/", response_model=APIResponse)
def get_text_response(user, prompt):
    return getGPTResponse(user, prompt)


