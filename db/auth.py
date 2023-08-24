from bson.objectid import ObjectId
from fastapi import HTTPException
from db._general import GeneralDbManipulator
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
    
    def checkEmailAvailability(self,email:str) -> bool:
        """
        Checks if the given email is available
        """
        return not self.getCollection('users','am').find_one({'email':email})
        

    def getUserById(self,id:str) -> dict:
        """
        Gets the user with the given id
        """
        result = self.getCollection('users','am').find_one({'_id':ObjectId(id)})
        if not result: raise HTTPException(status_code=400, detail="No such user")
        return result


    def createUser(self,email:str,password_hash:str) -> bool:
        """
        Creates a new user
        """
        return self.getCollection('users','am').insert_one({
            'email':email,
            'password_hash':password_hash,
            'priv_level':0,
            'metadata':{},
        }).inserted_id
    
    def deleteUser(self,id:str) -> bool:
        """
        Deletes the user with the given id
        """
        return self.getCollection('users','am').delete_one({'_id':ObjectId(id)}).acknowledged

