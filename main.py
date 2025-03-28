from fastapi import FastAPI

app=FastAPI()


vendas={
    1:{"item":"lata","preço_unitário":4,"quantidade":5},
    2:{"item":"lata","preço_unitário":4,"quantidade":5},
    3:{"item":"lata","preço_unitário":4,"quantidade":5},
    4:{"item":"lata","preço_unitário":4,"quantidade":5}
}

@app.get('/')
def home ():
    return {"vendas":len(vendas)}