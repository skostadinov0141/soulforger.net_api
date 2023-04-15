from fastapi import APIRouter, HTTPException, Request, Depends
from pymongo import MongoClient
from bson.objectid import ObjectId
from urllib.parse import quote_plus 
from routers.discord_authentication import validate_token
from models.character import DSACharacter
import bson
import yaml
import uuid



# region Database
secrets = None

with open(file='secrets.yaml', mode='r', encoding='utf8') as file:
    secrets = yaml.safe_load(file)

uri = "mongodb://%s:%s@%s" % (
    quote_plus(secrets['database_username']), 
    quote_plus(secrets['database_password']), 
    f"{secrets['database_ip']}:{secrets['database_port']}"
)

mongo = MongoClient(uri, serverSelectionTimeoutMS=5)

database = mongo['dsa_soulforger_net']
# endregion



# region Router
router = APIRouter(
    prefix='/characters/creation',
    tags=['characters']
)
# endregion



# region API Methods

@router.get('/get_schema')
async def get_character_schema():#(auth : bool = Depends(validate_token)):
    return DSACharacter()

# endregion