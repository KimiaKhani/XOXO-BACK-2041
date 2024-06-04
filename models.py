from sqlalchemy import Column, Integer,Float,String, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum

Base = declarative_base()


class GameStatus(str, Enum):
    WIN = 'WIN'
    LOSE = 'LOSE'



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, index=True, primary_key=True)
    name = Column(String)
    status = Column(ENUM(GameStatus), nullable=True)
