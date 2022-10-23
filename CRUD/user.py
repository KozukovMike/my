from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from models import create_session, User


class CRUDUser:

    @staticmethod
    @create_session
    def add(user, session=None):
        session.add(user)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(user)
            return user

    @staticmethod
    @create_session
    def get(user_id, session=None):
        user = session.execute(
            select(User)
            .where(User.id == user_id)
        )
        user = user.first()
        if user:
            return user[0]

    @staticmethod
    @create_session
    def all(session=None):
        users = session.execute(
            select(User)
            .order_by(User.id)
        )
        return [i[0] for i in users]

    @staticmethod
    @create_session
    def update(user, session=None):
        user = user.__dict__
        del user['_sa_instance_state']
        session.execute(
            update(User)
            .where(User.id == user['id'])
            .values(**user)
        )
        try:
            session.commit()
        except IntegrityError:
            return False
        else:
            return True

    @staticmethod
    @create_session
    def delete(user_id, session=None):
        session.execute(
            delete(User)
            .where(User.id == user_id)
        )
        session.commit()

