from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# Настройка базы данных
#SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Используем SQLite для простоты
SQLALCHEMY_DATABASE_URL = "postgresql://fastuser:fastpassword@127.0.0.1:5432/mydb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Модель User для базы данных
class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)


class Example(Base):
    __tablename__ = "examples"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    description2 = Column(String)

# Создание таблиц в базе данных
def init_db():
    Base.metadata.create_all(bind=engine)
