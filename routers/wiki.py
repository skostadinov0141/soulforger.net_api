from typing import Optional
from fastapi import APIRouter, HTTPException, Request, Depends, Response
from db._db_manager import DbManager
from models.account_management.account import Account, Login
from bson.objectid import ObjectId
from urllib.parse import quote_plus 
from dotenv import load_dotenv
from models.profile_management.profile_management import Profile
from models.wiki.wiki_search_query import WikiSearchQuery
from validators.account_management import validate_pw, validate_email
from pprint import pprint
from routers.account_management import authenticate
from validators.profiles import validateProfile


db = DbManager()


# region Router
router = APIRouter(
    prefix='/wiki',
    tags=['Wiki']
)
# endregion


# region Endpoints

@router.post('/search')
async def search(request: Request, query: WikiSearchQuery, user_id: ObjectId = Depends(authenticate)):
    return db.wiki.findEntriesByTags(query.tags)

@router.get('/tags')
async def get_unique_tags(request: Request, user_id: ObjectId = Depends(authenticate)):
    return db.wiki.findUniqueTags()

@router.get('/sub-categories')
async def get_unique_sub_categories(request: Request, category: str, user_id: ObjectId = Depends(authenticate)):
    return db.wiki.findUniqueSubCategories(category)

@router.get('/titles')
async def get_unique_titles(request: Request, user_id: ObjectId = Depends(authenticate)):
    return db.wiki.findUniqueTitles()

@router.get('/entry')
async def find_entry(request: Request, entry_id: str, user_id: ObjectId = Depends(authenticate)):
    return db.wiki.findEntryById(entry_id)

# endregion