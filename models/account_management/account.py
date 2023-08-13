from pydantic import BaseModel

class Account(BaseModel):
    email: str
    displayName: str
    passwordConfirmation: str
    password: str
    eula: bool

class Login(BaseModel):
    email: str
    password: str
    remember: bool