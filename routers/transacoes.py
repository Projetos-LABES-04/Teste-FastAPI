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


transacoes_db = [
    {"id": 1, "conta": "123", "data": "2025-03-30", "valor": 15000.00, "localizacao": "SP", "status": "normal"},
    {"id": 2, "conta": "456", "data": "2025-03-30", "valor": 20000.00, "localizacao": "RJ", "status": "suspeita"}
]
