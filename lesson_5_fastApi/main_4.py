# Обработка запросов POST
# Этот код создает приложение FastAPI и добавляет обработчик POST-запросов для
# URL-адреса /items/. Функция create_item() принимает объект Item и возвращает его
# же.


import logging
from fastapi import FastAPI
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()
@app.post("/items/")
async def create_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item