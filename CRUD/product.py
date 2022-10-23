from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from models import create_session, Product


class CRUDProduct:

    @staticmethod
    @create_session
    def add(product, session=None):
        session.add(product)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(product)
            return product

    @staticmethod
    @create_session
    def get(product_id, session=None):
        product = session.execute(
            select(Product)
            .where(Product.id == product_id)
        )
        product = product.first()
        if product:
            return product[0]

    @staticmethod
    @create_session
    def all(session=None):
        products = session.execute(
            select(Product)
            .order_by(Product.id)
        )
        return [i[0] for i in products]

    @staticmethod
    @create_session
    def update(product, session=None):
        product = product.__dict__
        del product['_sa_instance_state']
        session.execute(
            update(Product)
            .where(Product.id == product['id'])
            .values(**product)
        )
        try:
            session.commit()
        except IntegrityError:
            return False
        else:
            return True

    @staticmethod
    @create_session
    def delete(product_id, session=None):
        session.execute(
            delete(Product)
            .where(Product.id == product_id)
        )
        session.commit()
