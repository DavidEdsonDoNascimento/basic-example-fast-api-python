from fastapi import FastAPI
from in_memory import get_products

app = FastAPI()


@app.get("/")
def get_products_route():
    
    products = get_products()
    
    return {"products": products}