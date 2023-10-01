from bson import ObjectId
from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from db._db_manager import DbManager
from models.auth import Registration
from validators.account_management import validate_pw, validate_email
from datetime import datetime, timedelta
import os
import bcrypt


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
    user = db.auth.getUserByEmail(form_data.username)
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
            return {'access_token': encoded_jwt,'token_type': 'bearer', 'exp': data['exp']}


def validate_token(token:str = Depends(oauth_scheme)) -> dict:
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    return decoded_token


def get_user_id(token:dict = Depends(validate_token)) -> ObjectId:
    return ObjectId(token['sub'])


def validate_priv_level(decoded_token, required_levels: list):
    # Create a list of priv codes that are always allowed
    always_allowed = ['100','50']
    if always_allowed[0] in decoded_token["priv_level"] or always_allowed[1] in decoded_token["priv_level"]:
        return True
    if set(required_levels).issubset(decoded_token["priv_level"]) == False:
        raise HTTPException(status_code=401, detail="Insufficient privileges") 
    return True


@router.post('/register', description='Creates a new user')
def register(user_data:Registration):
    # Validate the data
    if user_data.eula != True:
        raise HTTPException(status_code=400, detail="You must agree to the EULA")
    if validate_pw(user_data.password)['result'] == False:
        raise HTTPException(status_code=400, detail="Password does not meet requirements")
    if validate_email(user_data.email)['result'] == False:
        raise HTTPException(status_code=400, detail="Email does not meet requirements")
    # Check if the username is already in use
    if db.auth.checkEmailAvailability(user_data.email) == False:
        raise HTTPException(status_code=400, detail="Email already in use")
    # Hash the password
    hashed_pw = bcrypt.hashpw(user_data.password.encode(), bcrypt.gensalt())
    # Create the user
    user_id = db.auth.createUser(user_data.email, hashed_pw.decode())
    db.profile.createProfile(user_id, user_data.displayName)
    return {'success': True}


@router.delete('/delete', description='Deletes the user')
def delete_user(token:dict = Depends(get_user_id)):
    db.profile.deleteProfile(token)
    db.privileges.deletePrivEscalationRequestsFromUser(token)
    return db.auth.deleteUser(token)

# endregion