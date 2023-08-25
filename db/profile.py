from datetime import datetime, timedelta
from bson import ObjectId
from fastapi import HTTPException
from db._general import GeneralDbManipulator
import cloudinary
from models.user.profile import ProfileInternal, ProfilePatch


class ProfileDbManipulator(GeneralDbManipulator):

    def __init__(self) -> None:
        super().__init__()    
    

    def getProfile(self,id:ObjectId) -> dict:
        """
        Gets the user's profile
        """
        result = self.getCollection('profiles','am').find_one(
            {'owner':id},
            {
                '_id':0,
                'owner':{'$toString':'$owner'},
                'display_name':1,
                'bio':1,
                'profile_picture':1,
                'preferred_role':1,
                'preferred_games':1,
                'badges':1,
            }
        )
        if not result: raise HTTPException(status_code=400, detail="No such profile")
        return result
    

    def createProfile(self,id:ObjectId,display_name:str) -> ObjectId:
        """
        Creates a new profile
        """
        return self.getCollection('profiles').insert_one(
            ProfileInternal(display_name=display_name,owner=id).toDict()
        ).inserted_id
    

    def deleteProfile(self,owner:ObjectId) -> bool:
        """
        Deletes a profile
        """
        return self.getCollection('profiles').delete_one(
            {'owner':owner}
        ).acknowledged


    def updateProfile(self,id:ObjectId,profile:ProfilePatch) -> bool:
        """
        Updates the user's profile
        """
        return self.getCollection('profiles').update_one(
            {'owner':id},
            {'$set':profile.dict(exclude_unset=True)}
        ).acknowledged
