from bson import ObjectId
from fastapi import UploadFile
from pydantic import BaseModel

class Badge(BaseModel):
    name: str
    description: str
    color: str
    style: str

class ProfilePatch(BaseModel):
    display_name: str | None = None
    bio: str | None = None
    profile_picture: UploadFile | None
    preferred_role: str | None = None
    preferred_games: list[str] | None = None
    badges: list[Badge] | None = None

class Profile(BaseModel):
    display_name: str
    bio: str
    profile_picture: UploadFile
    preferred_role: str
    preferred_games: list[str]
    badges: list[Badge]

class ProfileInternal():
    def __init__(self,display_name:str,owner:ObjectId) -> None:
        self.display_name = display_name
        self.owner = owner
        self.bio: str = ""
        self.profile_picture: str = ""
        self.preferred_role: str = ""
        self.preferred_games: list[str] = []
        self.badges: list[Badge] = []

    def toDict(self):
        return vars(self)
    