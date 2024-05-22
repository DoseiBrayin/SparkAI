from fastapi import APIRouter
from models.responseModel import APIResponse
from onboarding.infrastructure.onboardingInfra import login
from onboarding.models.loginModel import LoginModel

router = APIRouter()

@router.post("/login")
def login_user(login_user: LoginModel, response_model=APIResponse):
    return login(login_user)

