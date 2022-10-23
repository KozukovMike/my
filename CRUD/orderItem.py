from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from models import create_session, OrderItem


class CRUDOrderItem:

    @staticmethod
    @create_session
    def add(order_item, session=None):
        session.add(order_item)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(order_item)
            return order_item

    @staticmethod
    @create_session
    def get(order_item_id, session=None):
        order_item = session.execute(
            select(OrderItem)
            .where(OrderItem.id == order_item_id)
        )
        order_item = order_item.first()
        if order_item:
            return order_item[0]

    @staticmethod
    @create_session
    def all(session=None):
        order_items = session.execute(
            select(OrderItem)
            .order_by(OrderItem.id)
        )
        return [i[0] for i in order_items]

    @staticmethod
    @create_session
    def update(order_item, session=None):
        order_item = order_item.__dict__
        del order_item['_sa_instance_state']
        session.execute(
            update(OrderItem)
            .where(OrderItem.id == order_item['id'])
            .values(**order_item)
        )
        try:
            session.commit()
        except IntegrityError:
            return False
        else:
            return True

    @staticmethod
    @create_session
    def delete(order_item_id, session=None):
        session.execute(
            delete(OrderItem)
            .where(OrderItem.id == order_item_id)
        )
        session.commit()

