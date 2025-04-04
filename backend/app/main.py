 # Ponto de entrada da API
from fastapi import FastAPI
from routes import transacao_routes, conta_routes, notificacao_routes, dashboard_routes, auth_routes


app=FastAPI()

#Adiciona essas rotas à sua aplicação principal

app.include_router(transacao_routes.router)
app.include_router(conta_routes.router)
app.include_router(notificacao_routes.router)
app.include_router(dashboard_routes.router)
app.include_router(auth_routes.router)

