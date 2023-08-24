from typing import Annotated
from bson import ObjectId
from fastapi import APIRouter, Depends, UploadFile
from db._db_manager import DbManager
from models.auth.account import PrivEscalationRequest
from models.user.profile import Profile, ProfilePatch
from routers.auth import get_user_id, validate_priv_level, validate_token
from datetime import datetime
from cloudinary.uploader import upload, destroy
from typing import Annotated


db = DbManager()


# region Router
router = APIRouter(
    prefix='/user/profile',
    tags=['Profiles']
)
# endregion

# region API Methods


@router.get('', description='Returns the user\'s profile')
def get_profile(token:ObjectId = Depends(get_user_id)):
    return db.profile.getProfile(token)


@router.patch('', description='Updates the user\'s profile')
def update_profile(profile:ProfilePatch, token:ObjectId = Depends(get_user_id)):
    if profile.profile_picture and isinstance(profile.profile_picture, UploadFile):
        upload(profile.profile_picture.file, folder='profile_pictures', public_id=token)
        profile.profile_picture = f"profile_pictures/{token}"
    if profile.profile_picture and isinstance(profile.profile_picture, str):
        destroy(f"profile_pictures/{token}")
        profile.profile_picture = None
    return db.profile.updateProfile(token, profile)


# endregion