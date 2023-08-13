from pymongo.database import Database
from pymongo.collection import Collection
from bson.objectid import ObjectId
from db.general import GeneralDbManipulator


class AccountDbManipulator(GeneralDbManipulator):

    def __init__(self) -> None:
        super().__init__()


    """
    _summary_ : Gets the user with the given email
    _email_ : str
    _returns_ : dict
    """
    def getUser(self,email:str):
        return self.getCollection('users','am').find_one({'email':email})
    

    def createUser(self,email:str,passwordHash:str,displayName:str,eula:bool):
        return self.getCollection('users','am').insert_one({
            'email':email,
            'passwordHash':passwordHash,
            'displayName':displayName,
            'eula':eula,
            'privLevel':0
        })