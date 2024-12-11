
from app.schemas import UserCreate, User
from app.database import SessionLocal, UserModel, init_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


class UserService:
    @staticmethod
    def create_user(user_data: UserCreate, db: Session) -> User:
        db_user = UserModel(name=user_data.name, email=user_data.email)
        db.add(db_user)
        try:
            db.commit()
            db.refresh(db_user)
        except IntegrityError:
            db.rollback()
            raise ValueError("Email is already registered")
        return UserModel(id=db_user.id, name=db_user.name, email=db_user.email)

    @staticmethod
    def get_users(db: Session) -> list:
        return db.query(UserModel).all()
