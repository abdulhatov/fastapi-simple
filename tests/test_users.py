from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, init_db
from app.schemas import UserCreate

client = TestClient(app)

# Настройка для очистки базы данных перед тестами
def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Тестирование создания пользователя
def test_create_user():
    user_data = {"name": "John Doe", "email": "john2.doe@example.com"}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john2.doe@example.com"

# Тестирование получения списка пользователей
def test_list_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) > 0
