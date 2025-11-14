from fastapi import APIRouter
from schemas.user import UserCreate, UserResponse

router = APIRouter()

fake_db = {}

@router.post("/", response_model=UserResponse)
async def create_user(data: UserCreate):
    fake_db[data.email] = data.dict()
    return UserResponse(email=data.email, id=len(fake_db))

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    for i, (email, user) in enumerate(fake_db.items(), start=1):
        if i == user_id:
            return UserResponse(email=email, id=user_id)
    return {"error": "User not found"}
