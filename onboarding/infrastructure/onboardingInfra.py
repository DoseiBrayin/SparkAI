from db.conection import Session
from models.responseModel import APIResponse
from onboarding.models.loginModel import LoginModel
from onboarding.models.signUpModel import SignUpModel
from db.models.sparkDbModel import User,Gender,Payment,Personality
from fastapi import HTTPException
import uuid


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
            gender = session.query(Gender).get(signUp.fk_gender)
            payment = session.query(Payment).get(signUp.fk_payment)
            personality = session.query(Personality).get(signUp.fk_personality)

            newUser = User(
                id=str(uuid.uuid4()),
                name=signUp.name,
                email=signUp.email,
                password=signUp.password,
                age_range=signUp.age_range,
                gender=gender,
                payment=payment,
                personality=personality
            )
            session.add(newUser)
            session.commit()
            return APIResponse(status="Success", message="User Created", data=newUser.to_dict(),status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=APIResponse(status="Failed", message="Internal Server Error", data=str(e),status_code=500).__dict__)
    finally:
        session.close()

