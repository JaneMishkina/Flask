from typing import List

from HW_06.database import SessionLocal
from models import User, Order, Product
from schemas import UserSchema, OrderSchema, ProductSchema

from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.post("/users/", response_model=UserSchema)
async def create_user(user: UserSchema):
    db = SessionLocal()
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/users/", response_model=List[UserSchema])
async def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    return users


@router.post("/orders/", response_model=OrderSchema)
async def create_order(order: OrderSchema):
    db = SessionLocal()
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


@router.get("/orders/", response_model=List[OrderSchema])
async def get_orders():
    db = SessionLocal()
    orders = db.query(Order).all()
    return orders


@router.post("/products/", response_model=ProductSchema)
async def create_product(product: ProductSchema):
    db = SessionLocal()
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.get("/products/", response_model=List[ProductSchema])
async def get_products():
    db = SessionLocal()
    products = db.query(Product).all()
    return products

