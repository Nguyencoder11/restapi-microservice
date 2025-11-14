from fastapi import FastAPI
from routers.user import router as user_router

app = FastAPI(title="User Service")
app.include_router(user_router, prefix="/users")
