from fastapi import APIRouter
from schemas.auth import LoginRequest, TokenResponse
import jwt
import datetime

SECRET = "SUPER_SECRET"

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
async def login(data: LoginRequest):
    payload = {
        "email": data.email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
    }
    token = jwt.encode(payload, SECRET, algorithm="HS256")
    return TokenResponse(access_token=token)

@router.get("/verify")
async def verify(token: str):
    try:
        decoded = jwt.decode(token, SECRET, algorithms=["HS256"])
        return {"valid": True, "data": decoded}
    except:
        return {"valid": False}
