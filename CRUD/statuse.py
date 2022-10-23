from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from models import create_session, Status


class CRUDStatus:

    @staticmethod
    @create_session
    def add(status, session=None):
        session.add(status)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(status)
            return status

    @staticmethod
    @create_session
    def get(status_id, session=None):
        status = session.execute(
            select(Status)
            .where(Status.id == status_id)
        )
        status = status.first()
        if status:
            return status[0]

    @staticmethod
    @create_session
    def all(session=None):
        statuses = session.execute(
            select(Status)
            .order_by(Status.id)
        )
        return [i[0] for i in statuses]

    @staticmethod
    @create_session
    def update(status, session=None):
        status = status.__dict__
        del status['_sa_instance_state']
        session.execute(
            update(Status)
            .where(Status.id == status['id'])
            .values(**status)
        )
        try:
            session.commit()
        except IntegrityError:
            return False
        else:
            return True

    @staticmethod
    @create_session
    def delete(status_id, session=None):
        session.execute(
            delete(Status)
            .where(Status.id == status_id)
        )
        session.commit()

