from typing import Optional
from fastapi import APIRouter, HTTPException, Request, Depends, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from db._db_manager import DbManager
from models.account_management.account import Account, Login, PrivEscalationRequest
from validators.account_management import validate_pw, validate_email
from datetime import datetime, timedelta
import os
import bcrypt
from pymongo.cursor import Cursor


db = DbManager()


# region Router
router = APIRouter(
    prefix='/auth',
    tags=['Authentication']
)
# endregion



# region API Methods

oauth_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')

SECRET_KEY = os.getenv('JWT_SECRET_KEY')
ALGORITHM = os.getenv('JWT_ALGORITHM')


@router.post('/login', description='Returns an Access Token')
async def login(request: Request, form_data:OAuth2PasswordRequestForm = Depends(), remember: bool = False):
    # Search the database for a user with the given username (usernames are unique identifieres within the database)
    user = db.accounts.getUserByEmail(form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    else:
        # Compare the saved hash and the recieved password
        if not bcrypt.checkpw(form_data.password.encode(),user['password_hash'].encode()):
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        else:
            # If the data checks out generate an Access Token
            data = {}
            data['sub'] = str(user['_id'])
            if remember == True:
                data['exp'] = datetime.utcnow() + timedelta(weeks=24)
            else:
                data['exp'] = datetime.utcnow() + timedelta(hours=24)
            data['priv_level'] = user['priv_level']
            encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
            return {'access_token': encoded_jwt,'token_type': 'bearer'}


def validate_token(token:str = Depends(oauth_scheme)) -> dict:
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    return decoded_token


def validate_priv_level(decoded_token, required_level:int):
    if decoded_token["priv_level"] < required_level:
        raise HTTPException(status_code=401, detail="Insufficient privileges")
    return True


@router.post('/register', description='Creates a new user')
def register(user_data:Account):
    # Validate the data
    if validate_pw(user_data.password)['result'] == False:
        raise HTTPException(status_code=400, detail="Password does not meet requirements")
    if validate_email(user_data.email)['result'] == False:
        raise HTTPException(status_code=400, detail="Email does not meet requirements")
    # Check if the username is already in use
    if db.accounts.getUser(user_data.email) != None:
        raise HTTPException(status_code=400, detail="Email already in use")
    # Hash the password
    hashed_pw = bcrypt.hashpw(user_data.password.encode(), bcrypt.gensalt())
    # Create the user
    db.accounts.createUser(user_data.email, hashed_pw.decode(), user_data.displayName, user_data.eula)
    return {'success': True}


@router.post('/privileges/priv-escalation-request', description='Creates a priv escalation request')
def request_priv_escalation(priv_request: PrivEscalationRequest, token:dict = Depends(validate_token)):
    validate_priv_level(token, 0)
    priv_request_dict = priv_request.dict()
    priv_request_dict['user_id'] = token['sub']
    priv_request_dict['request_date'] = datetime.utcnow()
    # TODO: add priv mapping
    return db.accounts.requestPrivEscalation(priv_request_dict, 30)


@router.get('/privileges/priv-escalation-request', description='Returns a list of all priv escalation requests')
def get_priv_escalation_requests(page:int|None = None, page_size:int|None = None,token:dict = Depends(validate_token)):
    validate_priv_level(token, 30)
    if page and page_size:
        return list(db.accounts.paginate(db.accounts.getPrivEscalationRequests(), page, page_size)) 
    return list(db.accounts.getPrivEscalationRequests())

@router.get('/privileges/priv-escalation-request/{id}', description='Returns a priv escalation request with the given id')
def get_priv_escalation_request(id:str,token:dict = Depends(validate_token)):
    validate_priv_level(token, 30)
    return db.accounts.getPrivEscalationRequest(id)

@router.put('/privileges/priv-escalation-request/{id}', description='Updates a priv escalation request with the given id')
def update_priv_escalation_request(id:str, token:dict = Depends(validate_token)):
    priv_request = db.accounts.getPrivEscalationRequest(id)
    validate_priv_level(token, priv_request['approval_level'])
    return db.accounts.updatePrivEscalationRequest(priv_request)
    
# endregion