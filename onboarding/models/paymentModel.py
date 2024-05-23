from pydantic import BaseModel
from typing import Any

class PaymentModel(BaseModel):
    token: str
    state: bool
    date: Any 