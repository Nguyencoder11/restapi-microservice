from fastapi import FastAPI
from routers.product import router as product_router

app = FastAPI(title="Product Service")
app.include_router(product_router, prefix="/products")
