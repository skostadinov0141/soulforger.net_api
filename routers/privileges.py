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
    prefix='/user/privileges',
    tags=['Privileges']
)
# endregion



# region API Methods


@router.post('/escalation-request', description='Creates a priv escalation request')
def request_priv_escalation(priv_request: PrivEscalationRequest, token:dict = Depends(validate_token)):
    validate_priv_level(token, 0)
    priv_request_dict = priv_request.dict()
    priv_request_dict['user_id'] = token['sub']
    priv_request_dict['request_date'] = datetime.utcnow()
    # TODO: add priv mapping
    return db.privileges.requestPrivEscalation(priv_request_dict, 30)


@router.get('/escalation-request', description='Returns a list of all priv escalation requests')
def get_priv_escalation_requests(page:int|None = None, page_size:int|None = None,token:dict = Depends(validate_token)):
    validate_priv_level(token, 30)
    if page and page_size:
        return list(db.privileges.paginate(db.privileges.getPrivEscalationRequests(), page, page_size)) 
    return list(db.privileges.getPrivEscalationRequests())


@router.get('/escalation-request/{id}', description='Returns a priv escalation request with the given id')
def get_priv_escalation_request(id:str,token:dict = Depends(validate_token)):
    validate_priv_level(token, 30)
    return db.privileges.getPrivEscalationRequest(id)


@router.put('/escalation-request/{id}', description='Updates a priv escalation request with the given id')
def update_priv_escalation_request(id:str, token:dict = Depends(validate_token)):
    priv_request = db.privileges.getPrivEscalationRequest(id)
    validate_priv_level(token, priv_request['approval_level'])
    return db.privileges.updatePrivEscalationRequest(priv_request)

# endregion