from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, VARCHAR, create_engine
from settings2 import DATABASE_URL

Base = declarative_base()


class Category(Base):
    __tablename__: str = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(150), nullable=False, unique=True)
    descr = Column(VARCHAR(150), nullable=False, unique=False)


engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


def create_session(func):
    def wrapper(**kwargs):
        with Session() as session:
            return func(session=session, **kwargs)
    return wrapper


@create_session
def add(category, session=None):
    session.add(category)
    try:
        session.commit()
    except IntegrityError:
        return None
    else:
        session.refresh(category)
        return category


category = Category(
    name='1',
    descr='check'
)
add(category=category)
