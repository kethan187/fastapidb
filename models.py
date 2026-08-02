from sqlalchemy import Column, Integer, String , Boolean
from database import Base

class criminals(Base):
    __tablename__ = "criminals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    gender = Column(String(10), nullable= False)
    location= Column(String(50),nullable=False)
    alias= Column(String(40),unique=True)
    password = Column(String(30),nullable=False)

class cricketers(Base):
    __tablename__ = "cricketers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    category=Column(String(40), nullable=False)
    iplteam= Column(String(50),nullable=False)
    alias= Column(String(40),unique=True)


class footballers(Base):
    __tablename__ = "footballers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    category=Column(String(40), nullable=False)
    teamname= Column(String(50),nullable=False)
    alias= Column(String(40),unique=True)


class animals(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    category=Column(String(40), nullable=False)
    height = Column(Integer)
    weight = Column(Integer)
  

class singers(Base):
    __tablename__ = "singers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    topsong = Column(String(40),nullable=True)
    awards = Column(String(40),nullable=False)
    location = Column(String(40),nullable=False)


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(25), nullable=False)
    alias = Column(String(40), unique=True, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)
    password = Column(String(300), nullable=False)