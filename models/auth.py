from datetime import datetime
from pydantic import BaseModel

class Registration(BaseModel):
    """
    Represents a user registration request.

    Attributes:
        email (str): The user's email address.
        displayName (str): The user's display name.
        passwordConfirmation (str): The user's password confirmation.
        password (str): The user's password.
        eula (bool): Whether the user has agreed to the terms of service.
    """
    email: str
    displayName: str
    passwordConfirmation: str
    password: str
    eula: bool

class Login(BaseModel):
    """
    Represents a user login request.

    Attributes:
        email (str): The user's email address.
        password (str): The user's password.
        remember (bool): Whether or not to remember the user's login.
    """

    email: str
    password: str
    remember: bool

class PrivEscalationRequest(BaseModel):
    """
    Represents a request for privilege escalation.

    Attributes:
        reason (str): The reason for the privilege escalation request.
        requested_level (int): The level of privilege being requested.
        metadata (dict): Additional metadata associated with the request.
    """
    reason: str
    requested_level: int
    metadata: dict
