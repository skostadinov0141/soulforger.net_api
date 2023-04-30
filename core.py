from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from routers import character_creation
from routers import account_management
from routers import skill_checks

from uuid import uuid4
from dotenv import load_dotenv
import os

app = FastAPI()

origins = ["http://localhost:5173", "http://soulforger.net:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(character_creation.router)
app.include_router(account_management.router)
app.include_router(skill_checks.router)

@app.middleware("http")
async def add_session_id(request: Request, call_next):
    session_id = request.cookies.get("session_id")
    request.state.session_id = session_id or str(uuid4())
    response : Response = await call_next(request)
    response.set_cookie("session_id", value=request.state.session_id, httponly=True)
    print(request.state.session_id)
    return response