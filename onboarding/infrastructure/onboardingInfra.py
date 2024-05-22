from db.conection import Session
from models.responseModel import APIResponse
from onboarding.models.loginModel import LoginModel
from onboarding.models.signUpModel import SignUpModel
from db.models.sparkDbModel import User
from fastapi import HTTPException


def login(login: LoginModel):
    try:
        session = Session()
        user = session.query(User).filter(User.email == login.email, User.password == login.password).first()
        if user:
            return APIResponse(status="Success", message="Login Successfull", data=user.to_dict(),status_code=200)
        else:
            raise HTTPException(status_code=401, detail=APIResponse(status="Failed", message="Invalid Credentials", data=None,status_code=401).__dict__)
    except Exception as e:
        raise HTTPException(status_code=500, detail=APIResponse(status="Failed", message="Internal Server Error", data=str(e),status_code=500).__dict__)
    finally:
        session.close()

def signUp(signUp: SignUpModel):
    try:
        session = Session()
        user = session.query(User).filter(User.email == signUp.email).first()
        if user:
            raise HTTPException(status_code=401, detail=APIResponse(status="Failed", message="User Exists", data=None,status_code=401).__dict__)
        else:
            newUser = User(
                id=signUp.id,
                name=signUp.name,
                email=signUp.email,
                password=signUp.password,
                age_range=signUp.age_range,
                gender=signUp.gender,
                payment=signUp.payment,
                personality=signUp.personality
            )
            session.add(newUser)
            session.commit()
            user_dict = {key: value for key, value in newUser.__dict__.items() if key != '_sa_instance_state'}
            return APIResponse(status="Success", message="User Created", data=user_dict,status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=APIResponse(status="Failed", message="Internal Server Error", data=str(e),status_code=500).__dict__)
    finally:
        session.close()

