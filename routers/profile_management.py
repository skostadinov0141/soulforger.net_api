from typing import Optional
from fastapi import APIRouter, HTTPException, Request, Depends, Response
from db._db_manager import DbManager
from models.account_management.account import Account, Login
from bson.objectid import ObjectId
from urllib.parse import quote_plus 
from dotenv import load_dotenv
from models.profile_management.profile_management import Profile
from validators.account_management import validate_pw, validate_email
from pprint import pprint
from routers.account_management import authenticate
from validators.profiles import validateProfile


db = DbManager()


# region Router
router = APIRouter(
    prefix='/profiles',
    tags=['Profiles']
)
# endregion


# region Endpoints

@router.get('/user')
async def get_user_data( request: Request, user_id: ObjectId = Depends(authenticate)):
    user_obj = db.profiles.getProfileFromUser(user_id)
    del user_obj['_id']
    del user_obj['owner']
    return user_obj


@router.patch('/user')
async def update_profile(profile: Profile, user_id: ObjectId = Depends(authenticate)):
    validation = validateProfile(profile)
    if validation['result'] == False:
        raise HTTPException(status_code=400, detail=validation['details'])
    result = db.profiles.updateProfile(user_id, profile)
    del result['owner']
    del result['_id']
    return result

# endregion