from fastapi import FastAPI
from app.routers import users

app = FastAPI()

# Подключаем маршруты
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI project!"}