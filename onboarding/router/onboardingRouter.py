from fastapi import APIRouter
from models.responseModel import APIResponse
from onboarding.infrastructure.onboardingInfra import login, signUp
from onboarding.models.loginModel import LoginModel
from onboarding.models.signUpModel import SignUpModel

router = APIRouter()

@router.post("/login")
def login_user(login_user: LoginModel, response_model=APIResponse):
    return login(login_user)

@router.post("/signUp")
def signUp_user(signUp_user: SignUpModel, response_model=APIResponse):
    return signUp(signUp_user)
