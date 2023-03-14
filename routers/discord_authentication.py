from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from bson.objectid import ObjectId
from urllib.parse import quote_plus 
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
    prefix='/discord_auth',
    tags=['discord_auth']
)
# endregion



# region API Methods
@router.post('/register_account')
async def register_account(discord_id: str):
    # attempt to find an existing entry, if found raise error
    databaseEntry = database.users.find_one({'discord_id' : discord_id})
    if databaseEntry is not None:
        raise HTTPException(status_code=409, detail={
            'description' : 'Account already registered'
        })
    newEntry = {
        'uuid':uuid.uuid4(),
        'discord_id':discord_id
    }
    return newEntry
# endregion