from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: str


class OrderSchema(BaseModel):
    id: int
    userid: int
    productid: int
    orderdate: str
    orderstatus: str

class ProductSchema(BaseModel):
    id: int
    name: str
    description: str
    price: float