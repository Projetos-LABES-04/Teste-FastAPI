from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class Transacao(BaseModel):
    id: int
    conta: str
    data: str
    valor: float
    localizacao: str
    status: str  # normal, suspeita, em análise
