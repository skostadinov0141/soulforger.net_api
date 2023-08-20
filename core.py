import json
from fastapi import Depends, FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from routers import auth
from routers import user

from dotenv import load_dotenv
from uuid import uuid4
from dotenv import load_dotenv
import cloudinary
import os

load_dotenv('dsa_soulforger.env')

cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUDNAME'),
    api_key=os.environ.get('CLOUDINARY_APIKEY'),
    api_secret=os.environ.get('CLOUDINARY_APISECRET'),
    secure=True,
)

if os.path.exists('dsa_soulforger.env') == True:
    app = FastAPI()
else:
    app = FastAPI(docs_url=None, redoc_url=None)

origins = ["http://localhost:3000", "http://soulforger.net:5173", "https://soulforger.net", "https://beta.soulforger.net"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(character_creation.router)
app.include_router(auth.router)
app.include_router(user.router)