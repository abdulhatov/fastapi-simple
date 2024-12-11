from fastapi import APIRouter
from app.schemas import User, UserCreate
from app.database import create_user, get_users

router = APIRouter()

@router.post("/", response_model=User)
def create_new_user(user: UserCreate):
    return create_user(user)

@router.get("/", response_model=list[User])
def list_users():
    return get_users()