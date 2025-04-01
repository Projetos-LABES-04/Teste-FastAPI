from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

router=APIRouter()

class DashboardMetrics(BaseModel):
    total_transacoes: int
    transacoes_suspeitas: int
    contas_investigadas: int
    alertas_recentes: List[str]
