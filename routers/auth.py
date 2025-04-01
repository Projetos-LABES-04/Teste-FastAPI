from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router =APIRouter()


class LoginRequest(BaseModel):
    username: str
    password: str
