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
from utilities.characterSchemeGenerator import generateCombatSkillList, generateTalentList
from pymongo.collection import Collection
from yaml import safe_load


db = DbManager()


# region Router
router = APIRouter(
    prefix='/community/contribute',
    tags=['Community Contributions']
)
# endregion


#region API Endpoints

@router.get('/staged/unique-titles')
async def get_unique_staged_titles(user_id: ObjectId = Depends(authenticate)):
    return db.contributions.getUniqueStagedTitles()

@router.get('/comitted/unique-titles')
async def get_unique_comitted_titles(user_id: ObjectId = Depends(authenticate)):
    return db.contributions.getUniqueComittedTitles()

#endregion