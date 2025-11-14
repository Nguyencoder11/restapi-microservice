from fastapi import APIRouter, HTTPException
import requests

router = APIRouter()

AUTH_URL = "http://auth-service:8001/auth/verify"

products = [
    {"id": 1, "name": "Iphone"},
    {"id": 2, "name": "Macbook"},
]

@router.get("/")
async def get_products(token: str):
    res = requests.get(AUTH_URL, params={"token": token}).json()
    if not res.get("valid"):
        raise HTTPException(status_code=401, detail="Invalid token")

    return products
