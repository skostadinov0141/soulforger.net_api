from bson.objectid import ObjectId
from fastapi import HTTPException
from db.general import GeneralDbManipulator
from models.auth.account import PrivEscalationRequest
from datetime import datetime, timedelta


class AccountDbManipulator(GeneralDbManipulator):

    def __init__(self) -> None:
        super().__init__()


    def getUserByEmail(self,email:str) -> dict:
        """
        Gets the user with the given email
        """
        result = self.getCollection('users','am').find_one({'email':email})
        if not result: raise HTTPException(status_code=400, detail="No such user")
        return result
    

    def getUserById(self,id:str) -> dict:
        """
        Gets the user with the given id
        """
        result = self.getCollection('users','am').find_one({'_id':ObjectId(id)})
        if not result: raise HTTPException(status_code=400, detail="No such user")
        return result


    def createUser(self,email:str,password_hash:str,display_name:str,eula:bool) -> bool:
        """
        Creates a new user
        """
        return self.getCollection('users','am').insert_one({
            'email':email,
            'password_hash':password_hash,
            'display_name':display_name,
            'priv_level':0,
            'metadata':{},
            'profile_picture_url': None
        }).acknowledged

