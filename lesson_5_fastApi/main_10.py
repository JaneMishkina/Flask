# Работа с параметрами запроса и путями URL
# Часто клиенты отправляют запросы с параметрами, которые нужно обработать на
# сервере. В FastAPI параметры запроса и пути URL определяются в декораторах
# конечных точек.
from fastapi import FastAPI
app = FastAPI()
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# Этот код создает конечную точку для URL-адреса /items/{item_id}, которая
# принимает параметр item_id типа int и параметр q типа str со значением по
# умолчанию None. Если параметр q задан, функция возвращает JSON-объект с
# обоими параметрами, иначе — только с item_id.

@app.get("/users/{user_id}/orders/{order_id}")
async def read_item(user_id: int, order_id: int):
    # обработка данных
    return {"user_id": user_id, "order_id": order_id}

# Мы также можем определить несколько параметров URL-адреса в пути, например
# /users/{user_id}/orders/{order_id}, а затем определить соответствующие параметры в
# функции для доступа к ним.
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# В этом примере мы определяем новый маршрут /items/, который принимает два
# параметра запроса skip и limit. Значения по умолчанию для этих параметров равны
# 0 и 10 соответственно. Когда мы вызываем этот маршрут без каких-либо
# параметров запроса, он возвращает значения по умолчанию.
# Например, перейдя по адресу http://127.0.0.1:8000/items/ получим json c {"skip": 0,
# "limit": 10}.
