# Форматирование ответов API
# JSON объект
# В этом примере возвращается ответ JSON с настраиваемым сообщением и кодом состояния.
from fastapi import FastAPI
from fastapi.responses import JSONResponse
app = FastAPI()
@app.get("/message")
async def read_message():
    message = {"message": "Hello World"}
    return JSONResponse(content=message, status_code=200)