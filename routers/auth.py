from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router =APIRouter()


class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
