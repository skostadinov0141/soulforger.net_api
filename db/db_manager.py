import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from bson.objectid import ObjectId


class DbManager():

    def __init__(self):
        load_dotenv('dsa_soulforger.env')

        uri = "mongodb://%s:%s@%s/?authSource=%s" % (
            quote_plus(os.environ.get(f'DSA_SOULFORGER_DB_ACCOUNTMANAGER_UNAME')), 
            quote_plus(os.environ.get(f'DSA_SOULFORGER_DB_ACCOUNTMANAGER_PASS')), 
            f"{os.environ.get('DSA_SOULFORGER_DB_IP')}:{os.environ.get('DSA_SOULFORGER_DB_PORT')}",
            quote_plus(os.environ.get(f'DSA_SOULFORGER_DB_ACCOUNTMANAGER_SOURCE')),
        )

        mongo = MongoClient(uri, serverSelectionTimeoutMS=5)

        self.dbAccountManagerInstance : Database = mongo['dsa_soulforger_net']

        uri = "mongodb://%s:%s@%s/?authSource=%s" % (
            quote_plus(os.environ.get(f'DSA_SOULFORGER_DB_MISC_UNAME')), 
            quote_plus(os.environ.get(f'DSA_SOULFORGER_DB_MISC_PASS')), 
            f"{os.environ.get('DSA_SOULFORGER_DB_IP')}:{os.environ.get('DSA_SOULFORGER_DB_PORT')}",
            quote_plus(os.environ.get(f'DSA_SOULFORGER_DB_MISC_SOURCE')),
        )

        mongo = MongoClient(uri, serverSelectionTimeoutMS=5)

        self.dbMiscInstance : Database = mongo['dsa_soulforger_net']


    """Returns a Collection object based on the role defined by the asUser param."""
    def getCollection(self, collection_name: str, asUser: str = '') -> Collection:
        if(asUser == 'am'):
            return self.dbAccountManagerInstance[collection_name]
        return self.dbMiscInstance[collection_name]
    

    """Create a One to One relation between two dicts."""
    def createRelationOO(self,dict1: dict, rel_name1: str, dict2: dict, rel_name2: str) -> list:
        if '_id' in dict1 and '_id' in dict2:
            dict1[rel_name1] = dict2['_id']
            dict2[rel_name2] = dict1['_id']
        elif '_id' in dict1 and '_id' not in dict2:
            dict2['_id'] = ObjectId()
            dict1[rel_name1] = dict2['_id']
            dict2[rel_name2] = dict1['_id']
        elif '_id' not in dict1 and '_id' in dict2:
            dict1['_id'] = ObjectId()
            dict1[rel_name1] = dict2['_id']
            dict2[rel_name2] = dict1['_id']
        else:
            dict1['_id'] = ObjectId()
            dict2['_id'] = ObjectId()
            dict1[rel_name1] = dict2['_id']
            dict2[rel_name2] = dict1['_id']
        return [dict1, dict2]
    

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

    def getProfileFromUser(self, user_id: str) -> dict:
        return self.getCollection('profiles').find_one({'owner':user_id})
    
    """Check if an email already exists and is connected to a user"""
    def checkIfEmailExist(self,email:str):
        return self.getCollection('users','am').find_one({'email':email})