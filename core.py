from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import character_creation
from routers import account_management
from routers import skill_checks

from dotenv import load_dotenv
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(character_creation.router)
app.include_router(account_management.router)
app.include_router(skill_checks.router)