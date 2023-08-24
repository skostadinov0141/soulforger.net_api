import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from pymongo.cursor import Cursor
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

    

    def getCollection(self, collection_name: str, asUser: str = '') -> Collection:
        """Returns a Collection object based on the role defined by the asUser param."""
        if(asUser == 'am'):
            return self.dbAccountManagerInstance[collection_name]
        return self.dbMiscInstance[collection_name]
    

    def paginate(self, data: Cursor, page: int, page_size: int) -> list:
        """Returns a list of data objects based on the page and page_size params."""
        return list(data.skip(page * page_size).limit(page_size))
        
