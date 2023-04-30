from pydantic import BaseModel

class Account(BaseModel):
    email: str
    display_name: str
    password_confirmation: str
    password: str
    eula: bool

class Login(BaseModel):
    email: str
    password: str
    keep_logged_in: bool