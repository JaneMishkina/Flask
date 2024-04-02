# Настройка сервера и маршрутизации

# В этом примере мы определили две функции-обработчика запросов. Первая
# функция обрабатывает GET-запрос по корневому пути "/" и возвращает словарь с
# сообщением "Hello World". Вторая функция обрабатывает GET-запрос по пути
# "/items/{item_id}", где item_id — это переменная пути, а q — это параметр запроса.
# Функция возвращает словарь с переданными параметрами.

from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def read_root():
    return {"Hello": "World"}
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
