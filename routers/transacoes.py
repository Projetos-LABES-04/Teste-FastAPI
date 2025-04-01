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

@router.get("/", response_model=List[Transacao])
async def listar_transacoes(conta: Optional[str] = None, data: Optional[str] = None, status: Optional[str] = None):
    resultados = transacoes_db
    if conta:
        resultados = [t for t in resultados if t["conta"] == conta]
    if data:
        resultados = [t for t in resultados if t["data"] == data]
    if status:
        resultados = [t for t in resultados if t["status"] == status]
    return resultados

#Define um endpoint HTTP GET para obter os detalhes de uma transação específica identificada por transacao_id.
@router.get("/{transacao_id}", response_model=Transacao)
async def obter_transacao(transacao_id: int):
    for transacao in transacoes_db:
        if transacao["id"] == transacao_id:
            return transacao
    raise HTTPException(status_code=404, detail="Transação não encontrada")

@router.put("/{transacao_id}", response_model=Transacao)
async def atualizar_status_transacao(transacao_id: int, novo_status: str):
    for transacao in transacoes_db:
        if transacao["id"] == transacao_id:
            transacao["status"] = novo_status
            return transacao
    raise HTTPException(status_code=404, detail="Transação não encontrada")
