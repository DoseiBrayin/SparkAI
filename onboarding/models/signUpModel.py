from pydantic import BaseModel

class SignUpModel(BaseModel):
    name : str
    email : str
    password : str
    age_range : str
    fk_gender : str
    fk_payment : str = None
    fk_personality : str