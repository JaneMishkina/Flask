
from sqlalchemy import create_engine, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table, Column, create_engine, ForeignKey, DateTime
from sqlalchemy import Integer, String, Enum, DECIMAL

from project.models import OrderStatus

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    userid = Column(Integer, ForeignKey('users.id'))
    productid = Column(Integer)
    orderdate = Column(DateTime)
    orderstatus = Column(Enum(OrderStatus))


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)

# Инициализация таблиц в базе данных
Base.metadata.create_all(bind=engine)
