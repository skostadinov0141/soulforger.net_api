from typing import Annotated
from fastapi import APIRouter, Depends, UploadFile
from db._db_manager import DbManager
from models.auth.account import PrivEscalationRequest
from routers.auth import validate_priv_level, validate_token
from datetime import datetime
from cloudinary.uploader import upload, destroy
from typing import Annotated


db = DbManager()


# region Router
router = APIRouter(
    prefix='/user',
    tags=['Users']
)
# endregion



# region API Methods


@router.post('/privileges/priv-escalation-request', description='Creates a priv escalation request')
def request_priv_escalation(priv_request: PrivEscalationRequest, token:dict = Depends(validate_token)):
    validate_priv_level(token, 0)
    priv_request_dict = priv_request.dict()
    priv_request_dict['user_id'] = token['sub']
    priv_request_dict['request_date'] = datetime.utcnow()
    # TODO: add priv mapping
    return db.user.requestPrivEscalation(priv_request_dict, 30)


@router.get('/privileges/escalation-request', description='Returns a list of all priv escalation requests')
def get_priv_escalation_requests(page:int|None = None, page_size:int|None = None,token:dict = Depends(validate_token)):
    validate_priv_level(token, 30)
    if page and page_size:
        return list(db.user.paginate(db.user.getPrivEscalationRequests(), page, page_size)) 
    return list(db.user.getPrivEscalationRequests())


@router.get('/privileges/escalation-request/{id}', description='Returns a priv escalation request with the given id')
def get_priv_escalation_request(id:str,token:dict = Depends(validate_token)):
    validate_priv_level(token, 30)
    return db.user.getPrivEscalationRequest(id)


@router.put('/privileges/escalation-request/{id}', description='Updates a priv escalation request with the given id')
def update_priv_escalation_request(id:str, token:dict = Depends(validate_token)):
    priv_request = db.user.getPrivEscalationRequest(id)
    validate_priv_level(token, priv_request['approval_level'])
    return db.user.updatePrivEscalationRequest(priv_request)


@router.patch('/profile-picture' , description='Updates the user\'s profile picture')
def set_profile_picture(image_blob: UploadFile, token:dict = Depends(validate_token)):
    upload(image_blob.file, folder='profile_pictures', public_id=token['sub'])
    return db.user.setUserProfilePicture(token['sub'], f"profile_pictures/{token['sub']}")


@router.get('/profile-picture/{id}', description='Returns the user\'s profile picture')
def get_profile_picture(token:dict = Depends(validate_token)):
    return db.user.getUserProfilePicture(token['sub'])


@router.delete('/profile-picture', description='Deletes the user\'s profile picture')
def delete_profile_picture(token:dict = Depends(validate_token)):
    destroy(f"profile_pictures/{token['sub']}")
    return db.user.setUserProfilePicture(token['sub'], None)


# endregion