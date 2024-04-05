# Создание моделей для взаимодействия с таблицей в БД

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///mydatabase.db"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
)
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)

app = FastAPI()

class UserIn(BaseModel):
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)

class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)

# Первая модель нужна для получения информации о пользователе от клиента.
# Вторая используется для возврата данных о пользователе из БД клиенту.
