# Настройка FastAPI

# В этом примере мы создали объект FastAPI и определили конечную точку API с
# помощью декоратора @app.get("/"). Декоратор указывает, что это обработчик
# GET-запроса по пути "/".
# Внутри функции мы возвращаем словарь с сообщением "Hello World". Это
# сообщение будет отправлено в ответ на запрос.

from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}