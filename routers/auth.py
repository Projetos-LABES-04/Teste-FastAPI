from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router =APIRouter()


class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/login", response_model=TokenResponse)
async def login(login_data: LoginRequest):
    if login_data.username == "admin" and login_data.password == "senha123":
        return {"access_token": "token_exemplo"}
