import json
from fastapi import Depends, FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from routers import account_management

from uuid import uuid4
from dotenv import load_dotenv
import os


if os.path.exists('dsa_soulforger.env') == True:
    app = FastAPI()
else:
    app = FastAPI(docs_url=None, redoc_url=None)

origins = ["http://localhost:5173", "http://soulforger.net:5173", "https://soulforger.net", "https://beta.soulforger.net"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root():
    return {'message':'Hello World!'}

@app.get('/locked')
def locked(token:str = Depends(account_management.validate_token)):
    return token

# app.include_router(character_creation.router)
app.include_router(account_management.router)

# @app.middleware("http")
# async def add_session_id(request: Request, call_next):
#     session_id = request.cookies.get("auth_token")
#     request.state.session_id = session_id or str(uuid4())
#     response : Response = await call_next(request)
#     response.set_cookie("auth_token", value=request.state.session_id, httponly=True, secure=True)
#     return response