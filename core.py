from fastapi import FastAPI

from routers import discord_authentication
from routers import character_creation

app = FastAPI()

app.include_router(discord_authentication.router)
app.include_router(character_creation.router)