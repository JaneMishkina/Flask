# Валидация данных запроса и ответа
# #
# FastAPI позволяет автоматически валидировать данные запроса и ответа с
# помощью модуля pydantic. Например, можно создать класс Item для валидации
# данных:
# Этот код добавляет обработчики POST и PUT запросов, которые принимают объект
# Item и возвращают его же. Если данные не соответствуют описанию класса Item, то
# FastAPI вернет ошибку 422 с описанием ошибки.


import logging
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

class Item(BaseModel):
    """Этот класс содержит поля name, description, price и tax. Поля name и price
обязательны, а поля description и tax необязательны. """
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/")
async def read_root():
    logger.info('Отработал GET запрос.')
    return {"Hello": "World"}

@app.post("/items/")
async def create_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработал PUT запрос для item id = {item_id}.')
    return {"item_id": item_id, "item": item}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f'Отработал DELETE запрос для item id = {item_id}.')
    return {"item_id": item_id}
