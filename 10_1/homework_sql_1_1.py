from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey


Base = declarative_base()


class Category(Base):
    __tablename__: str = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(24), nullable=False, unique=True)


class Products(Base):
    __tablename__: str = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR(36), nullable=False)
    descr = Column(VARCHAR(140), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)


class Statuses(Base):
    __tablename__: str = 'statuses'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(10), unique=True)


class Users(Base):
    __tablename__: str = 'users'

    id = Column(Integer, primarykey=True)
    name = Column(VARCHAR(24))
    email = Column(VARCHAR(24), unique=True)


class Orders(Base):
    __tablename__: str = 'orders'

    id = Column(Integer, primarykey=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    status_id = Column(Integer, ForeignKey('statuses.id', ondekete='CASCADE'), nullable=False)


class OrderItems(Base):
    __tablename__: str = 'order_items'

    id = Column(Integer, primarykey=True)
    order_id = Column(Integer, ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'), nullable=False)
