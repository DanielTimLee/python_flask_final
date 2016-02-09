from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP


#
# max_length limit check needed!!
# String(1000) limit??

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    usrname = Column(String(20), unique=True)
    pwd = Column(String(20))
    email = Column(String(30), unique=True)
    text = Column(String(1000))
    created_date = Column(TIMESTAMP)

    def __init__(self, name=None, usrname=None, pwd=None, email=None, created_date=None):
        self.name = name
        self.usrname = usrname
        self.pwd = pwd
        self.email = email
        self.created_date = created_date

    def __repr__(self):
        return '<User %r %r %r %r %r>' % (self.name, self.usrname, self.pwd, self.email, self.created_date)

class Work(Base):
    __tablename__ = 'work'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    content = Column(String(1000))
    usrname = Column(String(20), unique=True)
    created_date = Column(TIMESTAMP)

    def __init__(self, title=None, usrname=None, content=None, created_date=None):
        self.title = title
        self.content = content
        self.usrname = usrname
        self.created_date = created_date

    def __repr__(self):
        return '<User %r %r %r %r>' % (self.title, self.usrname, self.content, self.created_date)

class Gallery(Base):
    __tablename__ = 'gallery'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    content = Column(String(1000))
    usrname = Column(String(20), unique=True)
    created_date = Column(TIMESTAMP)

    def __init__(self, title=None, usrname=None, content=None, created_date=None):
        self.title = title
        self.content = content
        self.usrname = usrname
        self.created_date = created_date

    def __repr__(self):
        return '<User %r %r %r %r>' % (self.title, self.usrname, self.content, self.created_date)

class Board(Base):
    __tablename__ = 'board'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    content = Column(String(1000))
    usrname = Column(String(20), unique=True)
    created_date = Column(TIMESTAMP)

    def __init__(self, title=None, usrname=None, content=None, created_date=None):
        self.title = title
        self.content = content
        self.usrname = usrname
        self.created_date = created_date

    def __repr__(self):
        return '<User %r %r %r %r>' % (self.title, self.usrname, self.content, self.created_date)
