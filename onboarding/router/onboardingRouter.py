from fastapi import APIRouter
from models.responseModel import APIResponse
from onboarding.infrastructure.onboardingInfra import login, signUp
from onboarding.models.loginModel import LoginModel
from onboarding.models.signUpModel import SignUpModel

router = APIRouter()

@router.post("/login", response_model=APIResponse)
def login_user(login_user: LoginModel):
    return login(login_user)

@router.post("/signUp", response_model=APIResponse)
def signUp_user(signUp_user: SignUpModel):
    return signUp(signUp_user)
