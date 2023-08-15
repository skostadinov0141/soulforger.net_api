from bson.objectid import ObjectId
from fastapi import HTTPException
from db.general import GeneralDbManipulator
from models.account_management.account import PrivEscalationRequest
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
            'metadata':{}
        }).acknowledged
    

    def requestPrivEscalation(self,priv_request: dict, approval_level:int) -> bool:
        """
        Creates a priv escalation request
        """
        return self.getCollection('priv_requests','am').insert_one({
            'reason':priv_request['reason'],
            'requested_level':priv_request['requested_level'],
            'user_id':ObjectId(priv_request['user_id']),
            'request_date':priv_request['request_date'],
            'expiration_date':datetime.utcnow() + timedelta(weeks=4),
            'metadata':priv_request['metadata'],
            'approval_level':approval_level,
        }).acknowledged
    

    def getPrivEscalationRequest(self,id:str) -> dict:
        """
        Gets a priv escalation requests with the given id
        """
        result = self.getCollection('priv_requests','am').find_one(
            {'_id':ObjectId(id)},
            {
                '_id': {'$toString': '$_id'}, 
                'reason': 1, 
                'requested_level': 1, 
                'user_id': {'$toString': '$user_id'}, 
                'request_date': 1, 
                'expiration_date': 1, 
                'metadata': 1, 
                'approval_level': 1
            }
        )
        if not result: raise HTTPException(status_code=400, detail="No such request")
        return result
    
    
    def getPrivEscalationRequests(self) -> list:
        """
        Gets all priv escalation requests
        """
        result = self.getCollection('priv_requests','am').find(
            {},
            {
                '_id': {'$toString': '$_id'}, 
                'reason': 1, 
                'requested_level': 1, 
                'user_id': {'$toString': '$user_id'}, 
                'request_date': 1, 
                'expiration_date': 1, 
                'metadata': 1, 
                'approval_level': 1
            },
        )
        return result

    
    def deletePrivEscalationRequest(self,id:str) -> dict:
        """
        Deletes a priv escalation request
        """
        return self.getCollection('priv_requests','am').delete_one({'_id':ObjectId(id)}).acknowledged

    def updatePrivEscalationRequest(self,priv_request:dict) -> bool:
        """
        Updates a priv escalation request
        """
        # Check if the user still exists
        user = self.getCollection('users','am').find_one({'_id':ObjectId(priv_request['user_id'])})
        if not user: raise HTTPException(status_code=400, detail="No such user")
        # Check if the user already has sufficient privileges
        if user['priv_level'] >= priv_request['requested_level']: 
            self.deletePrivEscalationRequest(priv_request['_id'])
            raise HTTPException(status_code=400, detail="User already has sufficient privileges")
        # Update the user's metadata
        user_metadata = user['metadata']
        for k,v in priv_request['metadata'].items():
            if type(v) == list:
                user_metadata[k] = list(set(user_metadata[k] + v))
            elif type(v) == dict:
                user_metadata[k] = {**user_metadata[k], **v}
            else:
                user_metadata[k] = v
        # Write the changes to the database
        result = self.getCollection('users','am').update_one(
            {'_id':ObjectId(priv_request['user_id'])},
            {'$set':{'priv_level':priv_request['requested_level'],'metadata':user_metadata}}
        ).acknowledged
        if result: self.deletePrivEscalationRequest(priv_request['_id'])
        return result


