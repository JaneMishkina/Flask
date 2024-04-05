# Формирование CRUD
# Создание пользователя в БД, create

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

@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(name=user.name, email=user.email)
    query = users.insert().values(**user.dict())
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}

# Мы определяем маршрут "/users/" для создания нового пользователя. В параметре
# функции мы ожидаем объект типа UserIn, который содержит имя и email
# пользователя. Затем мы создаем SQL-запрос на добавление новой записи в таблицу
# "users" с указанными данными. Выполняем запрос и возвращаем данные
# созданного пользователя, включая его ID.