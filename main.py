from fastapi import FastAPI
from routers import auth,dashboard,transacoes ,contas,notificacoes

app=FastAPI()

@app.get('/')
def home ():
    return "Hello World"