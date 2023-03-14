from fastapi import APIRouter, HTTPException, Request, Depends
from pymongo import MongoClient
from bson.objectid import ObjectId
from urllib.parse import quote_plus 
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
    prefix='/discord_auth',
    tags=['discord_auth']
)
# endregion



# region API Methods

def validate_token(req: Request):

    # Get unparsed token and split it i authToken and discordId
    unparsedToken = req.headers["Authorization"].split('%')
    authToken = unparsedToken[0]
    discordId = unparsedToken[1]

    # Find expected entry in DB
    entry = database.users.find_one({'discord_id':discordId})

    # Return true if auth conditions are met
    if entry is None:
        raise HTTPException(status_code=404, detail={
            'en':{
                'description':'No such account.'
            },
            'de':{
                'description':'Dieser Account existiert nicht.'
            }
        })
    if entry['auth_token'] != authToken:
        raise HTTPException(status_code=400, detail={
            'en':{
                'description':'The Auth-Token is not valid.'
            },
            'de':{
                'description':'Das Auth-Token ist falsch.'
            }
        })
    return True


@router.post('/register_account')
async def register_account(discord_id: str, discord_username: str):

    # attempt to find an existing entry, if found raise error
    databaseEntry = database.users.find_one({'discord_id' : discord_id})
    if databaseEntry is not None:
        raise HTTPException(status_code=409, detail={
            'en':{
                'description' : 'Account already registered.'
            },
            'de':{
                'description': 'Das Account wurde schon angemeldet.'
            }
        })
    
    # Generate entry
    newEntry = {
        'auth_token':str(uuid.uuid4()),
        'discord_id':discord_id,
        'discord_username':discord_username,
        'preferred_lang':'de',
        'discord_guilds':[],
        'active_sessions':[],
        'characters':[]
    }

    # ensure no collisions are present
    while database.users.find_one({'auth_token':newEntry['auth_token']}) is not None:
        newEntry['auth_token'] = str(uuid.uuid4())

    # write to DB
    database.users.insert_one(newEntry)
    return database.users.find_one({'auth_token': newEntry['auth_token']}, {'_id':False})


@router.delete('/{discord_id}/delete_account')
async def delete_account(discord_id: str):

    # Get entry from DB, if empty raise error
    entry = database.users.find_one({'discord_id': discord_id})
    if entry is None:
        raise HTTPException(status_code=404, detail={
            'en':{
                'description':'No such account.'
            },
            'de':{
                'description':'Dieser Account existiert nicht.'
            }
        })
    database.users.find_one_and_delete({'discord_id': discord_id})
    return {'result':'Deleted successfully.'}


@router.get('/{discord_id}/get_auth_token')
async def get_auth_token(discord_id:str):

    # get entry, if empty return 404 error
    entry = database.users.find_one({'discord_id': discord_id})
    if entry is None:
        raise HTTPException(status_code=404, detail={
            'en':{
                'description':'No such account.'
            },
            'de':{
                'description':'Dieser Account existiert nicht.'
            }
        })
    
    # return auth_token
    return f"{entry['auth_token']}%{entry['discord_id']}"


@router.patch('/{discord_id}/regen_auth_token')
async def regen_auth_token(discord_id:str):
    # get entry, if empty return 404 error
    entry = database.users.find_one({'discord_id': discord_id})
    if entry is None:
        raise HTTPException(status_code=404, detail={
            'en':{
                'description':'No such account.'
            },
            'de':{
                'description':'Dieser Account existiert nicht.'
            }
        })
    
    # Generate new UUID, keep generating until no match in DB
    entry['auth_token'] = str(uuid.uuid4())
    while database.users.find_one({'auth_token':entry['auth_token']}) is not None:
        entry['auth_token'] = str(uuid.uuid4())
    
    # Replace current auth_token with new unique one
    database.users.find_one_and_update({'discord_id':discord_id},{'$set':{'auth_token':entry['auth_token']}})
    return database.users.find_one({'discord_id': discord_id}, {'_id':False})
    
# endregion