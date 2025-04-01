from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

router=APIRouter()

class DashboardMetrics(BaseModel):
    total_transacoes: int
    transacoes_suspeitas: int
    contas_investigadas: int
    alertas_recentes: List[str]


@router.get("/", response_model=DashboardMetrics)
async def get_dashboard_metrics(periodo: Optional[str] = None):
        return {
        "total_transacoes": 1000,
        "transacoes_suspeitas": 50,
        "contas_investigadas": 10,
        "alertas_recentes": ["Alerta 1", "Alerta 2", "Alerta 3"]
    }
#Retorna um dicionário com dados estáticos que simulam os valores de métricas do dashboard. Em uma aplicação real, esses valores seriam obtidos a partir de consultas a um banco de dados ou de um serviço de analytics.