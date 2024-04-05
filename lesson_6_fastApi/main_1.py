# Определение моделей данных
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None
class User(BaseModel):
    username: str
    full_name: str = None
class Order(BaseModel):
    items: List[Item]
    user: User

# В этом примере определены три модели данных: Item, User и Order. Каждая модель
# данных содержит поля с указанными для них типами. Поле is_offer в модели Item
# имеет значение по умолчанию None.
