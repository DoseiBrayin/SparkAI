from fastapi import APIRouter, Depends
from models.responseModel import APIResponse
from onboarding.infrastructure.onboardingInfra import login, signUp, setPayment
from onboarding.models.loginModel import LoginModel
from onboarding.models.signUpModel import SignUpModel
from onboarding.models.paymentModel import PaymentModel
from JWT.JWTBearer import JWTBearer

router = APIRouter()

@router.post("/login", response_model=APIResponse)
def login_user(login_user: LoginModel):
    return login(login_user)

@router.post("/signUp", response_model=APIResponse)
def signUp_user(signUp_user: SignUpModel):
    return signUp(signUp_user)

@router.post("/payment", response_model=APIResponse)
def set_payment(payment: PaymentModel):
    return setPayment(payment)