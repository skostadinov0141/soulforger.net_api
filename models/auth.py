from datetime import datetime
from pydantic import BaseModel

class Registration(BaseModel):
    email: str
    displayName: str
    passwordConfirmation: str
    password: str
    eula: bool

class Login(BaseModel):
    email: str
    password: str
    remember: bool

class PrivEscalationRequest(BaseModel):
    reason: str
    requested_level: int
    metadata: dict
