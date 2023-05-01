from datetime import datetime as dt
import datetime
from dateutil import parser
from pymongo.database import Database
from pymongo.collection import Collection
from bson.objectid import ObjectId
from db.general import GeneralDbManipulator
from models.profile_management.profile_management import Profile


class ProfilesDbManipulator(GeneralDbManipulator):

    def __init__(self) -> None:
        super().__init__()


    """Get the user's profile through their ObjectId."""
    def getProfileFromUser(self, user_id: str) -> dict:
        result = self.getCollection('profiles').find_one({'owner':user_id})
        return result
    
    
    """Updates a user's profile"""
    def updateProfile(self, user_id: ObjectId, new_profile: Profile) -> dict:
        current_profile : dict = self.getProfileFromUser(user_id)
        for k,v in new_profile.dict().items():
            if k == 'joined_on':
                continue
            current_profile[k] = v
        self.getCollection('profiles').replace_one({'owner':current_profile['owner']},current_profile)
        return current_profile