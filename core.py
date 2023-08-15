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

# app.include_router(character_creation.router)
app.include_router(account_management.router)