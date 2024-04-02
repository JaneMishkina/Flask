# Автоматическая документация по API

# Существует два варианта документации API:
# -интерактивная документаци Swagger
# -альтернативная документация ReDoc.
#
# Интерактивная документация Swagger
# Swagger — это инструмент для создания и документирования API. FastAPI использует Swagger UI для
# генерации интерактивной документации, которая отображает все маршруты, параметры и модели данных,
# которые были определены в приложении.
# http://localhost:8000/docs
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