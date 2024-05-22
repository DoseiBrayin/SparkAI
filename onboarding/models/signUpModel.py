from pydantic import BaseModel

class SignUpModel(BaseModel):
    id: str
    name: str
    email: str
    password: str
    age_range: str
    personality: str
    gender: str
    payment: str = None