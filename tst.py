from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("mysql+pymysql://root:daniel@localhost/flask?charset=utf8:", echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine, echo=True))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models
    Base.metadata.create_all(bind=engine)


init_db()
