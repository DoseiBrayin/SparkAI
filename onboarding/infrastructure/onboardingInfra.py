from db.conection import Session
from models.responseModel import APIResponse
from onboarding.models.loginModel import LoginModel
from onboarding.models.signUpModel import SignUpModel
from db.models.usersModel import User
from fastapi import HTTPException


def login(login: LoginModel):
    try:
        session = Session()
        user = session.query(User).filter(User.email == login.username, User.password == login.password).first()
        if user:
            return APIResponse(status="Success", message="Login Successfull", data=user,status_code=200)
        else:
            raise HTTPException(status_code=401, detail=APIResponse(status="Failed", message="Invalid Credentials", data=None,status_code=401).__dict__)
    except Exception as e:
        raise HTTPException(status_code=500, detail=APIResponse(status="Failed", message="Internal Server Error", data=str(e),status_code=500).__dict__)
    finally:
        session.close()

