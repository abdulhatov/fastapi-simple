from fastapi import FastAPI
from app.routers import users
from app.database import init_db

app = FastAPI()

# Инициализация базы данных
init_db()

# Подключаем маршруты
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI project with clean architecture and real DB!"}
