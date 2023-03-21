from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import discord_authentication
from routers import character_creation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(discord_authentication.router)
app.include_router(character_creation.router)