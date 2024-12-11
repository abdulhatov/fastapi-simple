from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import User, UserCreate
from app.services.user_service import UserService
from app.database import SessionLocal, init_db

router = APIRouter()

# Зависимость для получения базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=User)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(user, db)

@router.get("/", response_model=list[User])
def list_users(db: Session = Depends(get_db)):
    return UserService.get_users(db)
