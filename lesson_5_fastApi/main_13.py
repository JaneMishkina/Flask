# Форматирование ответов API
# FastAPI позволяет форматировать ответы API в различных форматах, например, в
# JSON или HTML. Для этого нужно использовать соответствующие функции модуля
# fastapi.responses.
# HTML текст
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello World</h1>"

# Этот код создает конечную точку для корневого URL-адреса, которая возвращает
# HTML-страницу с текстом "Hello World". Функция read_root() использует класс
# HTMLResponse для форматирования ответа в HTML.

