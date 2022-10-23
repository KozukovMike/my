from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from models import create_session, Order


class CRUDOrder:

    @staticmethod
    @create_session
    def add(order, session=None):
        session.add(order)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(order)
            return order

    @staticmethod
    @create_session
    def get(order_id, session=None):
        order = session.execute(
            select(Order)
            .where(Order.id == order_id)
        )
        order = order.first()
        if order:
            return order[0]

    @staticmethod
    @create_session
    def all(session=None):
        orders = session.execute(
            select(Order)
            .order_by(Order.id)
        )
        return [i[0] for i in orders]

    @staticmethod
    @create_session
    def update(order, session=None):
        order = order.__dict__
        del order['_sa_instance_state']
        session.execute(
            update(Order)
            .where(Order.id == order['id'])
            .values(**order)
        )
        try:
            session.commit()
        except IntegrityError:
            return False
        else:
            return True

    @staticmethod
    @create_session
    def delete(order_id, session=None):
        session.execute(
            delete(Order)
            .where(Order.id == order_id)
        )
        session.commit()

