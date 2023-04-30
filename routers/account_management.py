from typing import Optional
from fastapi import APIRouter, HTTPException, Request, Depends, Response
from db.db_manager import DbManager
from models.account_management.account import Account, Login
from pymongo import MongoClient
from bson.objectid import ObjectId
from urllib.parse import quote_plus 
from dotenv import load_dotenv
from models.profile_management import Profile
from validators.account_management import validate_pw, validate_email
from pprint import pprint
import datetime
import bson
import yaml
import uuid
import os
import bcrypt
import re


db = DbManager()


# region Router
router = APIRouter(
    prefix='/auth',
    tags=['Authentication']
)
# endregion



# region API Methods

def authenticate(request: Request) -> Optional[ObjectId]:
    session_id = request.state.session_id
    user = db.getUserFromSession(session_id)
    pprint(user)
    if user:
        return user
    else:
        raise HTTPException(status_code=401, detail='Not Authorized!')

@router.get('/validate-session')
async def get_user_data( request: Request, user_id: dict = Depends(authenticate)):
    if user_id:
        return {}
    raise HTTPException(status_code=401)

@router.get('/user')
async def get_user_data( request: Request, user_id: dict = Depends(authenticate)):
    existing_session = db.getSession(request.state.session_id)
    user_obj = db.getProfileFromUser(user_id)
    del user_obj['_id']
    del user_obj['owner']
    return user_obj


@router.post('/register')
async def register_account(acc: Account):
    # Validate email and password, store the results in a list of dicts
    validations = [
        validate_email(acc.email),
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
        pprint(final_result)
        raise HTTPException(400,final_details)
    # Hash pw and create an account in the DB if all inputs are valid
    hashedPWD = bcrypt.hashpw(acc.password.encode(), bcrypt.gensalt(rounds=14))
    user_account = {
        'email':acc.email,
        'password_hash':hashedPWD.decode(),
        'characters_list':[],
        'campaigns_list':[],
        'games_list':[],
        'community_contributions_list':[],
    }
    # Create needed collections and reference them
    profile : Profile = Profile(
        display_name=acc.display_name
    )
    # insert into database
    related_dicts = db.createRelationOO(dict1=user_account,rel_name1='profile_document',dict2=profile.dict(),rel_name2='owner')
    db.getCollection('users','am').insert_one(related_dicts[0])
    db.getCollection('profiles').insert_one(related_dicts[1])
    # compile return dict
    return_dict = db.getProfileFromUser(related_dicts[0]['_id'])
    del return_dict['owner']
    del return_dict['_id']
    return return_dict


@router.post("/login")
async def login(request: Request, login: Login):
    # Get user from DB and create a session object to save to the DB
    existing_session = db.getSession(request.state.session_id)
    # Check if a session already exists, if it does return true
    if existing_session:
        user_obj = db.getProfileFromUser(existing_session['user_id'])
        del user_obj['_id']
        del user_obj['owner']
        pprint(existing_session["expires_at"])
        user_obj['expires_at'] = existing_session["expires_at"].astimezone(tz=datetime.timezone.utc)
        pprint(user_obj['expires_at'])
        return user_obj
    user = db.checkIfEmailExist(login.email)
    if user and bcrypt.checkpw(login.password.encode(), user['password_hash'].encode()):
        session_id = request.state.session_id
        session_obj = {
            "session_id": session_id, 
            "user_id": user["_id"],
        }
        # Insert into DB
        db.getCollection('sessions','am').insert_one(session_obj)
        user_obj = db.getProfileFromUser(user['_id'])
        del user_obj['owner']
        del user_obj['_id']
        return user_obj
    else:
        raise HTTPException(status_code=400, detail="Passwort und E-Mail stimmen nicht überein.")
        
# endregion