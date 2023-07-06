import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from bson.objectid import ObjectId
from json import load

class GeneralDbManipulator():

    def __init__(self):
        if os.path.exists('dsa_soulforger.env'):
            load_dotenv('dsa_soulforger.env')

        
        testing: bool = os.environ.get('TESTING') == 'True'

        if testing:
            uri = "mongodb+srv://soulforgerTesting:%s@soulforgerdb.hmyeqw0.mongodb.net/?retryWrites=true&w=majority" % (
                quote_plus(os.environ.get(f'SOULFORGER_TESTING_PW')), 
            )
            mongo = MongoClient(uri, serverSelectionTimeoutMS=5)
            self.dbAccountManagerInstance : Database = mongo['soulforger_testing']
            self.dbMiscInstance : Database = mongo['soulforger_testing']
        else:
            uri = "mongodb+srv://soulforgerUserManager:%s@soulforgerdb.hmyeqw0.mongodb.net/?retryWrites=true&w=majority" % (
                quote_plus(os.environ.get(f'SOULFORGER_USER_MANAGER_PW')), 
            )
            mongo = MongoClient(uri, serverSelectionTimeoutMS=5)
            self.dbAccountManagerInstance : Database = mongo['soulforger']
            uri = "mongodb+srv://soulforgerGeneral:%s@soulforgerdb.hmyeqw0.mongodb.net/?retryWrites=true&w=majority" % (
                quote_plus(os.environ.get(f'SOULFORGER_GENERAL_PW')), 
            )
            mongo = MongoClient(uri, serverSelectionTimeoutMS=5)
            self.dbMiscInstance : Database = mongo['soulforger']

    

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