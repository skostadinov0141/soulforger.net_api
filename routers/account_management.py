from fastapi import APIRouter, HTTPException, Request, Depends
from models.account_management.account import Account
from pymongo import MongoClient
from bson.objectid import ObjectId
from urllib.parse import quote_plus 
from dotenv import load_dotenv
from validators.account_management import validate_pw, validate_email
from pprint import pprint
import bson
import yaml
import uuid
import os
import bcrypt
import re



# region Database

load_dotenv('dsa_soulforger.env')

uri = "mongodb://%s:%s@%s/?authSource=%s" % (
    quote_plus(os.environ.get('DSA_SOULFORGER_DB_ACCOUNTMANAGER_UNAME')), 
    quote_plus(os.environ.get('DSA_SOULFORGER_DB_ACCOUNTMANAGER_PASS')), 
    f"{os.environ.get('DSA_SOULFORGER_DB_IP')}:{os.environ.get('DSA_SOULFORGER_DB_PORT')}",
    quote_plus(os.environ.get('DSA_SOULFORGER_DB_ACCOUNTMANAGER_SOURCE')),
)

mongo = MongoClient(uri, serverSelectionTimeoutMS=5)

database = mongo['dsa_soulforger_net']
# endregion



# region Router
router = APIRouter(
    prefix='/auth',
    tags=['Authentication']
)
# endregion



# region API Methods

@router.post('/register')
async def register_account(acc: Account):
    print('here')
    # Validate email and password, store the results in a list of dicts
    validations = [
        validate_email(acc.email, database),
        validate_pw(acc.password)
    ]

    # iterate over the validation dicts and if any validation is false return a 400 Bad Request
    # additionally make sure that the eula has been accepted
    final_result = True
    final_details = []
    for i in validations:
        if i['result'] == False:
            final_result = False
        for d in i['details']:
            final_details.append(d)
    if acc.eula == False:
        final_result = False
        final_details.append({
            'category':'eula',
            'detail':'NONE'
        })
    if acc.password != acc.password_confirmation:
        final_result = False
        final_details.append({
            'category':'password_confirmation',
            'detail':'Die Passwörter stimmen nicht überein.'
        })
    if acc.display_name == '':
        final_result = False
        final_details.append({
            'category':'display_name',
            'detail':'Der Anzeigename darf nicht leer sein.'
        })
    if final_result == False:
        raise HTTPException(400,final_details)
    
    pprint(final_details)

    # Hash pw and create an account in the DB if all inputs are valid
    hashedPWD = bcrypt.hashpw(acc.password.encode(), bcrypt.gensalt(rounds=14))
    userProfile = {
        'email':acc.email,
        'password_hash':hashedPWD.decode(),
        'display_name':acc.display_name
    }
    # insert into database
    database['users'].insert_one(userProfile)
    return {'result' : True}

# endregion