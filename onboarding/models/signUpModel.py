from pydantic import BaseModel

class SignUpModel(BaseModel):
    name: str
    email: str
    password: str
    age_range: str
    personality: str
    gender: str