# Создание конечных точек API
# Конечная точка API — это URL-адрес, по которому клиент может отправлять запросы
# к серверу. В FastAPI определение конечных точек происходит с помощью
# декораторов.
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def read_root():
    return {"Hello": "World"}
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# Этот код создает две конечные точки: одну для корневого URL-адреса, другую для
# URL-адреса /items/{item_id}. Функции read_root() и read_item() обрабатывают
# GET-запросы и возвращают JSON-объекты