import datetime
from pydantic import BaseModel
from bson.objectid import ObjectId

class Profile(BaseModel):
    display_name: str
    joined_on: str = datetime.datetime.now(tz=datetime.timezone.utc)
    profile_picture: str = ''
    bio: str = ''
