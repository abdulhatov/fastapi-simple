from app.models import fake_users_db
from app.schemas import UserCreate, User

def create_user(user_data: UserCreate) -> User:
    new_user = {
        "id": len(fake_users_db) + 1,
        "name": user_data.name,
        "email": user_data.email,
    }
    fake_users_db.append(new_user)
    return User(**new_user)

def get_users() -> list:
    return fake_users_db