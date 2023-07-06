# from fastapi import APIRouter, HTTPException, Request, Depends
# from pymongo import MongoClient
# from bson.objectid import ObjectId
# from urllib.parse import quote_plus 
# from models.character_creation.character import DSACharacter
# from dotenv import load_dotenv
# import bson
# import yaml
# import uuid
# import os



# # region Database

# load_dotenv('dsa_soulforger.env')

# uri = "mongodb://%s:%s@%s/?authSource=%s" % (
#     quote_plus(os.environ.get('DSA_SOULFORGER_DB_MISC_UNAME')), 
#     quote_plus(os.environ.get('DSA_SOULFORGER_DB_MISC_PASS')), 
#     f"{os.environ.get('DSA_SOULFORGER_DB_IP')}:{os.environ.get('DSA_SOULFORGER_DB_PORT')}",
#     quote_plus(os.environ.get('DSA_SOULFORGER_DB_MISC_SOURCE')),
# )

# mongo = MongoClient(uri, serverSelectionTimeoutMS=5)

# database = mongo['dsa_soulforger_net']
# # endregion



# # region Router
# router = APIRouter(
#     prefix='/characters/creation',
#     tags=['characters']
# )
# # endregion



# # region API Methods

# @router.get('/get_schema')
# async def get_character_schema():#(auth : bool = Depends(validate_token)):
#     return DSACharacter()

# # endregion