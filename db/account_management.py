from pymongo.database import Database
from pymongo.collection import Collection
from bson.objectid import ObjectId
from db.general import GeneralDbManipulator


class AccountDbManipulator(GeneralDbManipulator):

    def __init__(self) -> None:
        super().__init__()

    """Gets a specific user based on session ID. Returns None if no such session is found."""
    def getUserFromSession(self, session_id: str) -> ObjectId | None:
        result = self.getCollection('sessions','am').find_one({'session_id':session_id})
        if result:
            return result['user_id']
        return None
    
    """Gets a specific user based on session ID. Returns None if no such session is found."""
    def getSession(self, session_id: str) -> ObjectId | None:
        result = self.getCollection('sessions','am').find_one({'session_id':session_id})
        if result:
            return result
        return None
    
    """Removes a session from the DB."""
    def deleteSession(self, session_id: str) -> ObjectId | None:
        result = self.getCollection('sessions','am').delete_one({'session_id':session_id})
        if self.getSession(session_id):
            return True
        return False

    """Check if an email already exists and is connected to a user"""
    def checkIfEmailExist(self,email:str):
        return self.getCollection('users','am').find_one({'email':email})