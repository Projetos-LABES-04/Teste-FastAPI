from fastapi import FastAPI
from routers import auth,dashboard,transacoes ,contas,notificacoes

app=FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Autenticação"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(transacoes.router, prefix="/transacoes", tags=["Transações"])
app.include_router(contas.router, prefix="/contas", tags=["Contas"])
