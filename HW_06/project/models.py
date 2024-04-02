from enum import StrEnum
from pydantic import BaseModel

class OrderStatus(StrEnum):
    READYTOSHIP = 'подготовлен к отгрузке'
    SHIPPED = 'отгружен'
    RECEIVED = 'получен'
    ISSUED = 'выпущен'
    COMPLETED = 'выполнен'
    NEW = 'новый'
    UPDATED = 'обновлен'
    CONFIRMED = 'подтвержден'
    PAYAWAIT = 'ожидает оплаты'
    EXPIRED = 'истекший'
    CANCELED = 'отменен'
    PAYRECEIVED = 'оплачен'


class User(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: str
    password: str



class Order(BaseModel):
    id: int
    userid: int
    productid: int
    orderdate: str
    orderstatus: OrderStatus

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float

