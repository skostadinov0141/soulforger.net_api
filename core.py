from fastapi import FastAPI

from routers import discord_authentication

app = FastAPI()

app.include_router(discord_authentication.router)