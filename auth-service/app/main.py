from fastapi import FastAPI
from routers.auth import router

app = FastAPI(title="Auth Service")
app.include_router(router, prefix="/auth")
