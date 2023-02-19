from sqlalchemy import create_engine
from sqlalchemy.orm import as_declarative, sessionmaker

engine = create_engine("sqlite:///subscriptions.db")
session_factory = sessionmaker(bind=engine)


@as_declarative()
class Base:
    pass
